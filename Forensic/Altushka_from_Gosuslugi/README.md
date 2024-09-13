# Altushka from Gosuslugi, easy

## Description



## Writeup

The task has to be done using NTFS file system only

1. Unzip the archive
2. Check for alternate data streams with ``` dir /R ``` 
2. You'll notice there's an alternate data stream drive.txt:gosuslugi$data
3. Read it using ```more < drive.txt:gosuslugi```


## Flag: tqlCTF{R4y4n_G05u5lug_n3_um3r_V_k0nc3_dr1v4}
