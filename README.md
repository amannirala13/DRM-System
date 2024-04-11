# DRM-System

This is novel DRM solution being built as a research initiative at VIT, Vellore.

**Authors: [Aman Kumar Nirala](https://github.com/amannirala13), [Kaivalya Sao](/), [Shashank Kothari](https://github.com/ShashankKothari-exe)**

<img src="https://github.com/amannirala13/DRM-System/blob/main/vit_ico.png" alt="vit_logo" style="zoom: 50%;" />

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



# License

This project is licensed under the terms of the custom license as outlined in the [LICENSE.md](https://github.com/amannirala13/DRM-System/blob/main/LICENSE.md) file. Use of the DRM System, including all associated software and documentation, is subject to the terms and conditions in this license. By using or contributing to the DRM System, you agree to abide by its terms.

Please review the license file for detailed information on permitted uses and restrictions. The project is for testing and feedback purposes only, and any use beyond this scope is strictly prohibited without prior written consent from the authors. Unauthorized use, duplication, or distribution of this software may result in legal action.

This initiative is part of ongoing research at Vellore Institute of Technology, Vellore, and aims to develop a novel DRM solution. Feedback and contributions to this project are welcome, but must comply with the project's licensing terms.

For more information on how to use, test, or contribute to the DRM System, please refer to the documentation provided in this repository.

## Verifying the integrity of license

To ensure the integrity and authenticity of the license agreement, all releases are digitally signed. You can verify the digital signature using the [public key](/) provided in this repository.

### Prerequisites

To verify the signature, you will need:
- OpenSSL installed on your system. You can check if it's already installed by running `openssl version` in your terminal. If not, please refer to [OpenSSL's official documentation](https://www.openssl.org/) for installation instructions.
- The public key file ([`PUBLIC_KEY.pem`](/)) from this repository.
- The signature file ([`signature.sig`]()) provided alongside the release.
- The original file you wish to verify ([`LICENSE.md`](/)).

### Steps to Verify

1. **Download the Public Key**:
   Download `PUBLIC_KEY.pem` from the repository to your local machine.

2. **Download the Signature File**:
   Download `signature.sig`, the signature file for the document or software you wish to verify.

3. **Verify the Signature**:
   Open your terminal and navigate to the directory containing the downloaded files. Run the following command to verify the signature:

   ```bash
   openssl dgst -sha256 -binary LICENSE.md | openssl pkeyutl -verify -pubin -inkey public_key.pem -sigfile signature.sig
   ```
   
   #### Authorized Signature
   
   ```ini
   tCO3eJQ512fwomh2kn7mZS8aIRRXVzsVqDp5Whmxa0skMx3o+B7K/TEsxwtc+Kkp
   DPnoL6EWD4Io6Ae1oieplPXxabTIzq4tPadgS7CuCk1Z9A/X5qJ/G0YnIjqDTuKl
   Ul3CnZ9UZ/QyiSz1/A71uPDEnSyBPtOgMNr8p6LSExOqVSpYTFmZJ6CkyHGeWTae
   nb0dKz9mXl/cfuUkdzjRoi0YSdf+FrAZVn0utOGXg8jqi9ac86NcdMECk2ZsAcZO
   dH5PDOJIArOrwcmEszNaS/JjPfkv85BUU/WhSkIVieQ0qJq7r8YmV7s2qeYGH2eo
   5NcT4meJrHVbv5Sy1QxEAQ==
   ```
   
   #### Public Key
   
   ```ini
   -----BEGIN PUBLIC KEY-----
   MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtKXiEQU20ZmQpa9ylH2e
   NbyXMpuPC5x73z57hWDiWp7PCAzQJPoGyOPMrUDVQeiYsVBLjUxVnJHELTApZyuw
   oPZOaepGlGoDBe2kKV1ExLIzsfUcIzJtzC7RFDxiediyhjKxd7bfb4HiZF2s0BUZ
   28AVsJp3UXhfzgVmu3+dRZsHFmcpacGX3tiFFPnpcDZEI4I/V9vX9KwoQnZBhKXL
   DfBXBgqKz2LITsVQLaYxmeVfarC5ssCJa/HHG2lSMVphVY0HcoMQkKfKn2I8et3Z
   k0bC1GmYPiqypb6b58+Bv8bNvzr8UQqn0JiZpZYatm9r+5GOouxEPPyEvjcIjVSA
   RwIDAQAB
   -----END PUBLIC KEY-----
   ```
   
   

---

© 2024 Aman Kumar Nirala, Kaivalya Sao, Shashank Kothari. All rights reserved.

---

*CAUTION: The full details and code is not published as the research is still under process. This repository has been made public for testing and feedback purpose. This is not the finished solution and any use of the current code by any third-party for commercial or peronal purpose other than testing locally is strictly prohibited, the respository owner(s) will not be responsible for any damage caused by the use of the current code.* 

