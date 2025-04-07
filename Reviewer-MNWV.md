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
        The results of DivideMix and IDO. 
        The experiment is conducted under the setting with pre-trained ResNet50, with SGD, lr = 2e-3, weight_decay = 1e-3, momentum=0.9, batch_size=64. 
        One epoch has 1000 iterations, and 100 epochs are trained. 
        We set stage 1 for 2 epochs, stage 2 for 98 epochs. 
        The experiments use an A100 80G GPU, running for 5 times.
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
        The results of Standard, UNICON, ELR, DeFT, DivideMix, DISC and IDO on CIFAR-10 with five different noise levels. 
        The experiment setting is followed CIFAR-100 setting in our paper.
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

### Table 3

<table border="1" cellspacing="0" cellpadding="5">
  <thead>
    <tr>
      <th>Model</th>
      <th>Method</th>
      <th>Clothing1M</th>
      <th>Food101N</th>
      <th>Webvision</th>
      <th rowspan="9">Implementation Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Scratch ResNet 50</td>
      <td>Standard</td>
      <td>64.3%</td>
      <td>74.8%</td>
      <td>70.7%</td>
      <td rowspan="8">
        The results of pre-trained and randomly initialized <br>
        models. <br>
        Train for 100 epochs using SGD with a learning rate <br>
        of 0.01. The learning rate is reduced by a factor of <br>
        10 at epochs 40 and 80, with a weight decay of 5e-4. <br>
        For scratch models, stage 1 lasts 30 epochs <br>
        and stage 2 lasts 70 epochs; <br>
        For pre-trained models, stage 1 lasts 5 epochs <br>
        and stage 2 lasts 95 epochs.
      </td>
    </tr>
    <tr>
      <td>Scratch ResNet 50</td>
      <td>GJS</td>
      <td>71.6%</td>
      <td>82.6%</td>
      <td>79.3%</td>
    </tr>
    <tr>
      <td>Scratch ResNet 50</td>
      <td>IDO</td>
      <td><b>72.7%</b></td>
      <td><b>85.4%</b></td>
      <td><b>79.6%</b></td>
    </tr>
    <tr>
      <td>Pre-trained ResNet 50</td>
      <td>Standard</td>
      <td>68.3%</td>
      <td>81.6%</td>
      <td>77.8%</td>
    </tr>
    <tr>
      <td>Pre-trained ResNet 50</td>
      <td>PLC</td>
      <td>74.0%</td>
      <td>83.4%</td>
      <td>80.8%</td>
    </tr>
    <tr>
      <td>Pre-trained ResNet 50</td>
      <td>ELR</td>
      <td>74.4%</td>
      <td>84.2%</td>
      <td>80.5%</td>
    </tr>
    <tr>
      <td>Pre-trained ResNet 50</td>
      <td>DISC</td>
      <td>73.7%</td>
      <td>87.9%</td>
      <td>81.5%</td>
    </tr>
    <tr>
      <td>Pre-trained ResNet 50</td>
      <td>IDO</td>
      <td><b>74.8%</b></td>
      <td><b>88.2%</b></td>
      <td><b>82.9%</b></td>
    </tr>
  </tbody>
</table>
