Programming Assignment 31 Due date: Monday, 18 April, 2016 Suppose a web site hosts large video file𝐹that anyone can download. Browsers who download the file need to make sure the file is authentic before displaying the content to the user. One approach is to have the web site hash the contents of𝐹 using a collision resistant hash and then distribute the resulting short hash value ℎ=𝐻(𝐹)to users via some authenticated channel (later on we will use digital signatures for this). Browsers would download the entire file𝐹, check that𝐻(𝐹) is equal to the authentic hash valueℎand if so, display the video to the user. Unfortunately, this means that the video will only begin playing after the entire file𝐹has been downloaded. Our goal in this project is to build a file authentication system that lets browsers authenticate and play video chunks as they are downloaded without having to wait for the entire file. Insteadofcomputingahashoftheentirefile,thewebsitebreaksthefileinto1𝐾𝐵 blocks (1024bytes). It computes the hash of the last block and appends the value to the second to last block. It then computes the hash of this augmented second to last block and appends the resulting hash to the third block from the end. This process continues from the last block to the first as in the following diagram:
Figure 1: hashing process The final hash valueℎ0– a hash of the first block with its appended hash – is distributed to users via the authenticated channel as above. Now,abrowserdownloadsthefile𝐹oneblockatatime,whereeachblockincludes the appended hash value from the diagram above. When the first block(𝐵0∥ℎ1) is received the browser checks that𝐻(𝐵0∥ℎ1)is equal toℎ0and if so it begins playing the first video block. When the second block(𝐵1∥ℎ2)is received the browser checks that𝐻(𝐵1‖ℎ2)is equal toℎ1and if so it plays this second 1Source: https://class.coursera.org/crypto-015/quiz/attempt?quiz_id=122 1
block. This process continues until the very last block. This way each block is authenticated and played as it is received and there is no need to wait until the entire file is downloaded. It is not difficult to argue that if the hash function𝐻is collision resistant then an attacker cannot modify any of the video blocks without being detected by the browser. Indeed, sinceℎ0=𝐻(𝐵0∥ℎ1)an attacker cannot find a pair(𝐵′ 0,ℎ′ 1)≠(𝐵 0,ℎ1)such thatℎ0=𝐻(𝐵0∥ℎ1)since this would break collision resistanceof 𝐻. Therefore after the first hash check the browser is convinced that both𝐵0and ℎ1are authentic. Exactly the same argument proves that after the second hash check the browser is convinced that both𝐵1andℎ2are authentic, and so on for the remaining blocks. In this project we will be using SHA256 as the hash function. For an implementation of SHA256 use an existing crypto library such as PyCrypto (Python), Crypto++ (C++), or any other. When appending the hash value to each block, please append it as binary data, that is, as 32 unencoded bytes (which is 256 bits). If the file size is not a multiple of 1KB then the very last block will be shorter than 1KB, but all other blocks will be exactly 1KB. Your task is to write code to compute the hashℎ0of a given file𝐹and to verify blocks of𝐹as they are received by the client. You can check your code by using it to hash a different file. In particular, the hex encodedℎ0for this video file is: 03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8