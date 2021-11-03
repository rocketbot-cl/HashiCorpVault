



# HashiCorp Vault
  
Interact with HashiCorp. Create, update and delete secrets in HashiCorp Vault.  

## Howto install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path
## How to use this module
  
In order to use this module, you have to already have a Vault in HashiCorp (it can be On-Premise or Cloud).
You will need to know the Cluster URL, Namespace where the secrets are stored in, the token of the user and the mount point of the secrets (secrets engines).

## Overview


1. Connects to HashiCorp Vault  
Connects to HashiCorp Vault to interact with

2. Read Secrets  
Send a request for read secrets stored in HashiCorp Vault

3. Create or Update Secrets  
Send a request to create or update secrets stored in HashiCorp Vault

4. Delete Secrets  
Send a request to delete secrets stored in HashiCorp Vault
### Updates


----
### OS

- windows

### Dependencies
- [**hvac**](https://pypi.org/project/hvac/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)