###############################################################################
#   Author:         Graham Picard (gpicard@kipp.org)
#   Created:        2018-05-11
#   Updated:        2018-05-21
#   Name:           Whetstone API Call
###############################################################################

import requests
import json


class Whetstone:
    """ Whetstone API handler:

        Use to perform basic get requests with the Whetstone API.
        All endpoints taken from the v2 API documentation at:

            https://github.com/WhetstoneEducation/API


        Description:
        
        Provide valid API credentials, and query any valid API (v2) endpoint.
        Results provided as a JSON string
                  
        Params:

        instance:   A valid whetstone instance (found at 
                    https://[instance].whetstoneeducation.com)
        apikey:     A valid API key taken from the Whetstone user settings 
                    (found at https://[instance].whetstoneeducation.com/me)
    """

    def __init__(self, instance, apikey):
        self.url = "https://" + instance + ".whetstoneeducation.com"
        self.authurl = self.url + "/auth/api"
        self.apikey = apikey
        self.token = self.get_token(instance, self.apikey, self.authurl)
        self.endpoints = {'users': '/api/v2/users',
                          'observations': '/api/v2/observations',
                          'meetings': '/api/v2/meetings',
                          'meeting_modules': '/api/v2/meetingmodules',
                          'schools': '/api/v2/schools',
                          'assignments': '/api/v2/assignments',
                          'scores': '/api/v2/scores',
                          'informals': '/api/v2/informals',
                          'rubrics': '/api/v2/rubrics',
                          'measurements': '/api/v2/measurements',
                          'measurement_groups': '/api/v2/measurementGroups',
                          'measurement_types': '/api/v2/measurementTypes',
                          'tags': '/api/v2/tags',
                          'grade': '/api/v2/grades',
                          'courses': '/api/v2/courses',
                          'period': '/api/v2/periods',
                          'track': '/api/v2/tracks',
                          'goaltype': '/api/v2/goalTypes',
                          'action_step_options': '/api/v2/actionstepopts',
                          'files': '/api/v2/files',
                          'videos': '/api/v2/videos',
                          'observation_tag_1': '/api/v2/observationtag1s',
                          'observation_tag_2': '/api/v2/observationtag2s',
                          'observation_tag_3': '/api/v2/observationtag3s',
                          'observation_tag_4': '/api/v2/observationtag4s',
                          'observation_type': '/api/v2/observationTypes',
                          'observation_modules': '/api/v2/observationModules',
                          'observation_label': '/api/v2/observationLabels',
                          'collaboration_type': '/api/v2/collaborationtypes',
                          'plu_event_location': '/api/v2/plueventlocations',
                          'plu_event_type': '/api/v2/plueventtypes',
                          'plu_series': '/api/v2/pluseries',
                          'plu_content_area': '/api/v2/plucontentareas',
                          'video_type': '/api/v2/videotypes',
                          'meeting_tag_1': '/api/v2/meetingtag1s',
                          'meeting_tag_2': '/api/v2/meetingtag2s',
                          'meeting_tag_3': '/api/v2/meetingtag3s',
                          'meeting_tag_4': '/api/v2/meetingtag4s',
                          'goal_options': '/api/v2/goalopts',
                          'user_tag_1': '/api/v2/usertag1s',
                          'user_tag_2': '/api/v2/usertag2s',
                          'user_tag_3': '/api/v2/usertag3s',
                          'user_tag_4': '/api/v2/usertag4s',
                          'user_tag_5': '/api/v2/usertag5s',
                          'user_tag_6': '/api/v2/usertag6s',
                          'user_tag_7': '/api/v2/usertag7s',
                          'user_tag_8': '/api/v2/usertag8s',
                          'rubric_tag_1': '/api/v2/rubrictag1s',
                          'rubric_tag_2': '/api/v2/rubrictag2s',
                          'rubric_tag_3': '/api/v2/rubrictag3s',
                          'rubric_tag_4': '/api/v2/rubrictag4s',
                          'event_tag_1': '/api/v2/eventtag1s'}

    def get_token(self, instance, apikey, authurl):
        """ Parse response token from Whetstone server to make get_data()
            calls.
        """

        res = requests.post(authurl, data={"apikey": apikey})
        response = json.loads(res.text)
        
        try:
            token = response['token']
            return token

        except KeyError:
            print("Invalid Instance or API key\n\nInstance:", instance,
                  "\nKey:", apikey, "\nServer Response:", response, "\n")
            raise

    def get_data(self, endpoint):
        """ Gather data from any API v2 endpoints  

            params
            endpoint:   must be a valid API v2 endpoint. Use endpoints
                        provided in the class
        """
           
        try:
            endpointurl = self.url + endpoint
            payload = {}
            headers = {'content-type': 'application/json',
                       'x-access-token': self.token,
                       'x-key': self.apikey}

            # make request
            res = requests.get(endpointurl, data=payload, headers=headers, stream=True)
            response = ("{endpoint} - Status Code: {code}"
                         .format(endpoint=endpoint, code=res.status_code))

            print(response)

            return res.text

        except ConnectionError:
            print("Error: endpoint does not exist\n")
            raise
