#TranslateComparison

The goal of this project is to provide an objective comparison between google translate and microsoft cognitive translate APIs.

Here you will find sample code on how to implement each in python, as well as a script that times each service in a typical API call for comparison.

Findings:

 - Each service provides a similar response time ( about 0.5s or 0.6s for my calls) for my implementation

 - Google traslate's API is simple to consume and requires a single get request with the key sent as a parameter. Response is returned as a JSON file.

 - Microsoft translate's API is comparably slow to get up and running. To request a translation, you must send a token with your get request. To obtain
   a token you must send a post request to a seperate endpoint with your subscription key provided as a header. A token expires after 10 minutes. 
   Practically speaking this means that you must either monitor the age of your token (I use python's pickle library to do this), set your server to
   update your token on a timer, or get a new token for every translation request (this will yield a noticable performance slowdown). Microsoft's server
   will reply with xml, so that must be parsed.

- Google translate's API is no longer free of charge.

- Microsoft translate's API is free up to 2 000 000 characters / month

Note:

- This project does not take into account any quality difference between the two services
- You will need a google translate api key (go to google developer console), and a microsoft cognitive servcies subscription key (go to microsoft azure dashboard)
