# IDS 721 Project1    Yuwei Zhang, Duke MIDS
### Continuous delivery for a static personal webpage

#### Background
The goal of this project is to achieve continuous delivery for a static personal webpage. The webpage template comes from OpenResumeTemplates.com.

Compared to hardcopy, a digital webpage is convenient. Candidates could send a short URL link to companies or recruiters, and recruiters could look at the Resume anytime anywhere with a network and a device.

Compared to a Resume file, a personal webpage allows for revision at any time, which just suits the candidates' needs.

Moreover, candidates can further add audios and videos on the webpage. It is useful for industries including film, music, advertising and so on.

For the above reasons, such a personal webpage is useful to job applicants.


#### Application
This web application is based on Python Flask and deployed by AWS Elastic Beanstalk. The application continuously delivers the latest version on Github.
- The content of the Resume locates at "./templates/index.html" and the HTML template has to be put under the fixed folder name "templates" for flask's recognization.
- The Python script of the application locates at "application.py". To make sure the Elastic Beanstalk, the name of the flask application needs to be "application.py" and the variable name of the flask instance also needs to be "application".

#### Potential problems during development
1. location of the HTML templates
2. name of the flask script and flask instance
3. the IAM policy
