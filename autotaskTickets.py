from base64 import encode
import json
import logging

import requests

def createTicket(autotaskAuthObj, ticketInformation):

    """ Generates an Autotask ticket. ticketInformation is a dictionary that contains:
        title
        description
        queueid
        companyID
        status
        Returns a dictionary with the resulting api status code as \"status_code\' and \'text\' as \'message\'."""

    create_ticket_request = requests.request("POST", f"{autotaskAuthObj.baseurl}/Tickets", headers=autotaskAuthObj.headers, data=ticketInformation)

    return {"status_code": create_ticket_request.status_code, "message": create_ticket_request.text}

def attachToTicket(autotaskAuthObj, ticketnumber, attachmentdict):

    """ Uploads an attachment to the specified ticket. The attachmentjson parameter is dictionary with the following keys:
        data      - base64 encoded file
        fullpath  - name of file as it will appear in AutoTask
        publish   - always should be set to 1
        title     - description of uploaded file
        attachmentType - should always be set to FILE_ATTACHMENT"""

    payload = json.dumps(attachmentdict)

    request_headers = autotaskAuthObj.headers
    request_headers['Content-Type'] = "application/json"

    attachment_request = requests.request("POST", f"{autotaskAuthObj.baseurl}/Tickets/{ticketnumber}/Attachments", headers=autotaskAuthObj.headers, data=payload)

    del request_headers['Content-Type']

    return {"status_code": attachment_request.status_code, "message": attachment_request.text}