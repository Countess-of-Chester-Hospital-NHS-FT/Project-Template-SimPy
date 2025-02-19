# Project Template (SimPy)

This git repository is a template that should be used as the default structure for new discrete event simulation projects. It was adapted from [NHSE template](https://github.com/nhsengland/nhse-repository-template/tree/main) and [BSOL template](https://github.com/Birmingham-and-Solihull-ICS/BSOLproject) . The structure of the DES model code and the streamlit app are adapted from material taught on the [HSMA Programme](https://hsma.co.uk/). It won't fit all circumstances perfectly, and you can adapt it to your needs and make a pull request if you want to suggest changes to the template.

The aim of this template is two-fold: firstly to give a common structure for analytical projects to aid
reproducibility and collaboration, secondly to allow for additional security settings as default to prevent accidental upload of files that should not be committed to Git and GitHub.

## To use this template, please use the following practises:

* This template assumes we are just using simulated data. If for any reason you are using real data create a `data` folder, put any data files in the `data` folder and add this folder to the .gitignore file.  A further layer of security is that all xls, xlsx, csv and pdf files are also explicit ignored in the whole folder as well.  ___If you need to commit one of these files, you must use the `-f` (force) command in `commit`, or specify the file as an exception in the .gitignore but you must be sure there is no identifiable data.__
* Adapt the .gitignore to suit your needs.
* Similarly, if you produce any documentation or outputs that are sensitive or contain personal data, create `docs` or `output` folders and add these to the .gitignore.
* Change the codeowners file (in .github folder) so you are the codeowner.
* Environment requirements are captured in the environment.yml (if you need additional packages etc make sure these are detailed in this file)

### Please also consider the following:
* Comment your code to make sure others can follow.
* Consider your naming conventions: we recommend `snake case` where spaces are replaced by underscores and no capitals are use. E.g. `outpatient_referral_data`

__Please update/replace this README file with one relevant to your project__

# Project Name

### Status
This project is currently work in progress / completed / being maintained / not being maintained

### About the project
Short description and purpose / objectives of the project e.g:

#### Problem: 
Poor patient flow is leading to long waits for admission in ED. This leads to poor performance against all the key ED wait metrics for the hospital and more importantly, there is evidence that long waits for admission in ED are associated with poorer outcomes for patients.
#### Management strategies: 
The two main strategies employed to tackle this problem is increasing the number of beds (by creation of escalation beds) and trying to decrease discharge delays (reducing length of stay). Additionally we have a Same Day Emergency Care (SDEC) facility and it is unclear how the number of people admitted through this facility impacts the waits of those in ED.
#### Key questions:
* Given x beds, how far does admitted length of stay have to reduce to meet particular waiting time targets for those queuing in ED? (Evidence based target)
* If we open 15 beds but keep admitted length of stay the same, what is the impact on ED waiting times and the various targets? (Evidence for a particular management strategy)
* What is the optimum number of people to stream from ED to SDEC to minimise ED waits? (Evidence for a particular management strategy)

Link to any refereneces / publications

Note: Only public or simulated data are shared in this repository

### Project Structure

* The model code is in the model.py file and the app can be launched using launch.py
* Any notes which may be helpful

### Built with
Captured in environment.yml

### Outputs
* Streamlit app which users can use to try different scenarios
* Report

### Contributing
Contributions and identification of issues are welcomed.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/Feature`)
3. Commit your Changes (`git commit -m 'Add some Feature'`)
4. Push to the Branch (`git push origin feature/Feature`)
5. Open a Pull Request

### License
Unless stated otherwise, the codebase is released under the MIT Licence. This covers both the codebase and any sample code in the documentation.

See LICENSE for more information.
