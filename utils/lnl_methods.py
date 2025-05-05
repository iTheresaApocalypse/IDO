import torch
from torch.nn import functional as F
import torch.nn as nn

class SCELoss(torch.nn.Module):
    def __init__(self, alpha, beta, num_classes=10, reduction="mean"):
        super(SCELoss, self).__init__()
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.alpha = alpha
        self.beta = beta
        self.num_classes = num_classes
        self.reduction = reduction
        self.cross_entropy = torch.nn.CrossEntropyLoss(reduction=reduction)

    def forward(self, pred, labels):
        # CCE
        ce = self.cross_entropy(pred, labels)

        # RCE
        pred = F.softmax(pred, dim=1)
        pred = torch.clamp(pred, min=1e-7, max=1.0)
        label_one_hot = torch.nn.functional.one_hot(labels, self.num_classes).float().to(self.device)
        label_one_hot = torch.clamp(label_one_hot, min=1e-4, max=1.0)
        rce = (-1*torch.sum(pred * torch.log(label_one_hot), dim=1))

        if self.reduction == "none":
            loss = self.alpha * ce + self.beta * rce
        else:
            loss = self.alpha * ce + self.beta * rce.mean()
        return loss

class ELRLoss(torch.nn.Module):
    def __init__(self, num_examp, num_classes=10, beta=0.7, lamb=3):
        super(ELRLoss, self).__init__()
        self.num_classes = num_classes
        self.target = torch.zeros(num_examp, self.num_classes).cuda()
        self.beta = beta
        self.lamb = lamb

    def cross_entropy(output, target):
        return F.cross_entropy(output, target)

    def forward(self, index, output, label):
        y_pred = F.softmax(output,dim=1)
        y_pred = torch.clamp(y_pred, 1e-4, 1.0-1e-4)
        y_pred_ = y_pred.data.detach()
        self.target[index] = self.beta * self.target[index] + (1-self.beta) * ((y_pred_)/(y_pred_).sum(dim=1,keepdim=True))
        ce_loss = F.cross_entropy(output, label, reduction="none")
        elr_reg = ((1-(self.target[index] * y_pred).sum(dim=1)).log())
        final_loss = ce_loss + self.lamb * elr_reg
        return final_loss


class WELoss(torch.nn.Module):
    def __init__(self, num_classes=10):
        super(WELoss, self).__init__()
        self.num_classes = num_classes

    def forward(self, output_s, output_w, prob1, prob2, cdf1, cdf2, label):
        # Convert prob to tensor and ensure it's on the same device
        prob_tensor = torch.from_numpy(prob1).to(output_s.device)

        y_pred_s = F.softmax(output_s, dim=1)
        y_pred_w = F.softmax(output_w, dim=1)
        y_pred_s = torch.clamp(y_pred_s, 1e-4, 1.0 - 1e-4)
        y_pred_w = torch.clamp(y_pred_w, 1e-4, 1.0 - 1e-4)

        # Calculate cross entropy loss without averaging
        ce_s = F.cross_entropy(output_s, label, reduction='none')
        ce_w = F.cross_entropy(output_w, label, reduction='none')
        ce_term = prob_tensor * (ce_s + ce_w)
        ce_term = ce_term.mean()

        # Calculate MSE loss, averaging over each sample
        mse = F.mse_loss(output_s, output_w, reduction='none').mean(dim=1)
        mse_weight = torch.tensor(prob1 * cdf1 + (1 - prob2) * (1 - cdf2)).to(output_s.device)
        mse_term = mse_weight * mse
        mse_term = mse_term.mean()

        # Average y_pred_s and y_pred_w first
        y_pred_avg = (y_pred_s + y_pred_w) / 2
        conf = torch.max(y_pred_avg, dim=1)[0]
        conf = conf.unsqueeze(1)
        
        # Calculate entropy of the averaged y_pred
        entropy_avg = -conf * torch.sum(y_pred_avg * torch.log(y_pred_avg), dim=1)

        # Calculate entropy_term
        entropy_term = (1 - prob_tensor) * entropy_avg
        entropy_term = entropy_term.mean()

        # Total loss
        total_loss = ce_term + mse_term + entropy_term
        return total_loss
