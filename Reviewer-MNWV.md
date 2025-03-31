## 📊 Figures and Tables

### Table 1

<table border="1" cellspacing="0" cellpadding="5">
  <thead>
    <tr>
      <th>Method</th>
      <th>Architecture</th>
      <th>Accuracy±std</th>
      <th>Time per Epoch</th>
      <th rowspan="3">Implementation Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DivideMix</td>
      <td>ResNet-50</td>
      <td>74.59±0.55</td>
      <td>717s</td>
      <td rowspan="2">
        The results of DivideMix and IDO. The experiment <br>
        is conducted under the setting with pre-trained ResNet50, <br>
        with SGD, lr = 2e-3, weight_decay = 1e-3, momentum=0.9, <br>
        batch_size=64. One epoch has 1000 iterations, and 100 epochs <br>
        are trained. We set stage 1 for 2 epochs, stage 2 for <br>
        98 epochs. The experiments use an A100 80G GPU, running for 5 times.
      </td>
    </tr>
    <tr>
      <td>IDO</td>
      <td>ResNet-50</td>
      <td><b>74.77±0.48</b></td>
      <td><b>229s</b></td>
    </tr>
  </tbody>
</table>


### Table 2

<table border="1" cellspacing="0" cellpadding="5">
  <thead>
    <tr>
      <th>Noise</th>
      <th>Architecture</th>
      <th>Sym. 20%</th>
      <th>Sym. 40%</th>
      <th>Sym. 60%</th>
      <th>Asym. 40%</th>
      <th>Inst. 40%</th>
      <th rowspan="8">Implementation Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Standard</td>
      <td>ResNet-50</td>
      <td>93.2%</td>
      <td>92.3%</td>
      <td>88.2%</td>
      <td>91.1%</td>
      <td>90.9%</td>
      <td rowspan="7">
        The results of Standard, <br>
        UNICON, ELR, DeFT, DivideMix, <br>
        DISC and IDO on CIFAR-10 <br>
        with five different noise levels. <br>
        The experiment setting is followed <br>
        CIFAR-100 setting in our paper.
      </td>
    </tr>
    <tr>
      <td>UNICON</td>
      <td>ResNet-50</td>
      <td>94.8%</td>
      <td>93.2%</td>
      <td>92.5%</td>
      <td>93.5%</td>
      <td>93.9%</td>
    </tr>
    <tr>
      <td>ELR</td>
      <td>ResNet-50</td>
      <td>96.5%</td>
      <td>95.8%</td>
      <td>95.1%</td>
      <td>95.2%</td>
      <td>94.8%</td>
    </tr>
    <tr>
      <td>DeFT</td>
      <td>CLIP-ResNet-50</td>
      <td>96.9%</td>
      <td>96.6%</td>
      <td>95.7%</td>
      <td>93.8%</td>
      <td>95.1%</td>
    </tr>
    <tr>
      <td>DivideMix</td>
      <td>ResNet-50</td>
      <td>97.1%</td>
      <td><b>96.9%</b></td>
      <td>96.3%</td>
      <td>93.1%</td>
      <td>96.0%</td>
    </tr>
    <tr>
      <td>DISC</td>
      <td>ResNet-50</td>
      <td>96.8%</td>
      <td>96.5%</td>
      <td>95.5%</td>
      <td>95.1%</td>
      <td><b>96.5%</b></td>
    </tr>
    <tr>
      <td>IDO</td>
      <td>ResNet-50</td>
      <td><b>97.3%</b></td>
      <td><b>96.9%</b></td>
      <td><b>96.5%</b></td>
      <td><b>95.3%</b></td>
      <td>96.4%</td>
    </tr>
  </tbody>
</table>

