# DRM-System

This is novel DRM solution being built as a research initiative at VIT, Vellore.

**Authors: [Aman Kumar Nirala](https://github.com/amannirala13), [Kaivalya Sao](/), [Shashank Kothari](https://github.com/ShashankKothari-exe)**

<img src="/Users/aman/Developer/DRMSystem/routine/DRM-System/vit_ico.png" alt="vit_logo" style="zoom: 50%;" />

# 🙋🏻‍♂️ How to use ?

Using the DRM soultion needs both hardware and software confugrations. This guide will help you setup your system to start testing the DRM solution.

First we need to setup the **DRM sub-module**. Typically it's simply interfacing the DRM kit with the GPIO of the system or make a serial connection with the CPU (depending on which model you opt for).

## ➬ GPIO Connection Guide

TODO: Provide the GPIO guide

## ➬ Serial Connection Guide

TODO: Provide the Serial guide

After the hardware is connected and tested, you can install the device driver or boot the system with the compatible kernel. *Check the kernel logs for verifying if the DRM sub-system is connected properly*.

After this setup is completed. Software distributers need to regester with our secured servers to start using the CI/CD services for on-demand secure file generation and delivery.

## 🔒 Embedding executable with security identifier

You will be using the `secure_id.py` for generating the secured executable from a regular executable. The script accepts two parameters with the first parameter is the current executable path and the second is the secured executable path which it will generate.

Example:

``````shell
python secure_id mytest.exec ./secured/mytest.exec
``````

This will generate a new file at `./secured/mytest.exec`.

This python file can be used to generate executables for your platform and added to the env path for direct terminal access and CI/CD integration.

The osX binaries are provided in the repository with the `secure_exe` and `secure_id` which can be used to perform secured execution and generating secured executable respectively.

## 🏃🏻 Securely executing the file

This section utilizes the exclusive syscalls in the supported kernels that identifies the secured executables and checks for it's validity before the executable is loaded in the memory. In this repository, you are provided with a python script `secure_exe.py` for proof of concept

which includes the near the truth implementation of the algorithm inside the extended systemcall in the kernel.

The `secure_exe.py` accepts one parameter which is the path of the secured executable that needs to be executed.

Example:

``````shell
python secure_exe ./secured/mytest.exec
``````

Now if the secured executable was built for your system, it will be loaded in the memory and executed, else it will be blocked from loading and an exception will be raised.

---

*CAUTION: The full details and code is not published as the research is still under process. This repository has been made public for testing and feedback purpose. This is not the finished solution and any use of the current code by any third-party for commercial or peronal purpose other than testing locally is strictly prohibited, the respository owner(s) will not be responsible for any damage caused by the use of the current code.* 

