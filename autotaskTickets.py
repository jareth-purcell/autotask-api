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

def attachToTicket(autotaskAuthObj, ticketnumber, encodedattachment):

    """ Uploads an attachment to the specified ticket. """

    payload = json.dumps({
        "data": f"{encodedattachment}",
        "fullPath": "bean.PNG",
        "publish": 1,
        "title": "King of England",
        "attachmentType": "FILE_ATTACHMENT"
    })

    request_headers = autotaskAuthObj.headers
    request_headers['Content-Type'] = "application/json"

    attachment_request = requests.request("POST", f"{autotaskAuthObj.baseurl}/Tickets/{ticketnumber}/Attachments", headers=autotaskAuthObj.headers, data=payload)

    del request_headers['Content-Type']

    return {"status_code": attachment_request.status_code, "message": attachment_request.text}