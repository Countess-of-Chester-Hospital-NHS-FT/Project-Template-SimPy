# DES model Open Code Checklist
This checklist is adapted from the [NHSE Repo Template](https://github.com/nhsengland/nhse-repository-template/blob/main/OPEN_CODE_CHECKLIST.md)
Please use this checklist to document adherence to best practice for published projects.

## When publishing your code you need to make sure:
  
### you’re clear about who owns the code and how others can use it

- [ ] Does your code have an appropriate licence and copyright notice?  (**Mandatory**)
- [ ] Is there a README and does it document intended purpose? (**Mandatory**)
- [ ] Is the README clear and concise? (**Optional** - use analytics unit template or [example](https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md))
- [ ] Do you need to consider MHRA 'software as a medical device' guidance? (**Mandatory** - use [flowchart](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/999908/Software_flow_chart_Ed_1-08b-IVD.pdf))
- [ ] Who has responsibility for ongoing support and communications for the code, including addressing any security concerns? (**Mandatory** Best practice to assign, else state the code is not maintained and when the last update was)
- [ ] Are package dependencies and libaries documented with versions? (**Optional**)
- [ ] Has the code been linked to any published outputs so others can easily link to the code? (**Optional**) 

### You do not release information that should remain closed

- [ ] Does the code include any sensitive, personal, secret or top secret data/information? (**Mandatory**)
- [ ] Does the code include any unreleased policy? (**Mandatory**)
- [ ] Does the code include business sensitive algorithms (e.g. finance allocations)? (**Mandatory**)
- [ ] Are the relevant stakeholders aware of this project? (**Mandatory**)
- [ ] Are any credentials contained in the source code or commits? (**Mandatory** - check in both current version and git history)
- [ ] Are any secret keys contained in the source code or commits? (**Mandatory** - check in both current version and git history)
- [ ] Are any SQL server addresses or connection strings in the source code or commits? (**Mandatory** - check in both current version and git history)
- [ ] Does the git history contain any sensitive information (e.g. at one time real data or credentials were in the code but have since been removed) (**Mandatory**)
- [ ] Have notebook outputs been removed/checked for sensitive information? (**Mandatory** - check but some appropriate outputs maybe useful: [Example]( https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.pre-commit-config.yaml))
- [ ] have you checked any screenshots or figures in your outputs and documentation for information that shouldn't be released? (**Mandatory**)

### You store it in a repository managed by your department (to make licensing/copyright clear)

- [ ] Is the code version controlled using GIT or similar? (**Optional**)
- [ ] Is the code stored in your organisational GitHub account? (**Optional**)

### An internal code review has been completed

- [ ] Has a colleague reviewed the code for sensitive data content and security vulnerabilities? (**Mandatory** - Best practice is to record automated code quality and security tools used)
- [ ] Has a code quality review been completed focussing on the end usability and clarity? (**Optional** - consider runing through the [example](https://best-practice-and-impact.github.io/qa-of-code-guidance/checklist_higher.html) or similar code quality checklist)
- [ ] Has the code undergone some level of testing.  The level of teting required will depend on the specific code and use-case but as minimum it should work in a fresh environment with arteficial data. (**Optional**)
