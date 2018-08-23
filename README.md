# A comparison between CPU vs GPU in executing tensorflow on iMac

## how to use
```
./run.sh report_filename_postfix
```

### change num of operations
* try 1, 3, 9, 25 ... 5279
```
vim list.txt
1 3 9 25 73 212 619 1808 5279

```

## requirements
* gnu time
```
brew install gtime
```

* python
  * numpy
  * matplotlib
  * tensorflow (compiled GPU)

## information
* A comparison between CPU vs GPU
  * Execution time of python command with "gtime command"
* e to the Nth power operations
* Please refer to source code for more information

## environments
* iMac14,2
* Intel Core i7
* 3.5 GHz
* num of processor: 1
* num of core:  4
* memory:    8 GB
* NVIDIA GeForce GTX 775M
* VRAM: 2048 MB
* tensorflow 1.10.0

## results
### overview
![GitHub Logo](/images/logo.png)
### zoom in
![GitHub Logo](/images/logo.png)
