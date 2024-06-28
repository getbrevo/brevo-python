# coding: utf-8

"""
    Brevo API

    Brevo provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/brevo  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   | 406  | Error. Not Acceptable  |   | 422  | Error. Unprocessable Entity |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@brevo.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetExtendedCampaignOverview(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'subject': 'str',
        'preview_text': 'str',
        'type': 'str',
        'status': 'str',
        'scheduled_at': 'str',
        'ab_testing': 'bool',
        'subject_a': 'str',
        'subject_b': 'str',
        'split_rule': 'int',
        'winner_criteria': 'str',
        'winner_delay': 'int',
        'send_at_best_time': 'bool',
        'utm_campaign_value': 'str',
        'utm_source': 'str',
        'utm_medium': 'str',
        'utm_id': 'int',
        'test_sent': 'bool',
        'header': 'str',
        'footer': 'str',
        'sender': 'GetExtendedCampaignOverviewSender',
        'reply_to': 'str',
        'to_field': 'str',
        'html_content': 'str',
        'share_link': 'str',
        'tag': 'str',
        'created_at': 'str',
        'modified_at': 'str',
        'inline_image_activation': 'bool',
        'mirror_active': 'bool',
        'recurring': 'bool',
        'sent_date': 'str',
        'return_bounce': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'subject': 'subject',
        'preview_text': 'previewText',
        'type': 'type',
        'status': 'status',
        'scheduled_at': 'scheduledAt',
        'ab_testing': 'abTesting',
        'subject_a': 'subjectA',
        'subject_b': 'subjectB',
        'split_rule': 'splitRule',
        'winner_criteria': 'winnerCriteria',
        'winner_delay': 'winnerDelay',
        'send_at_best_time': 'sendAtBestTime',
        'utm_campaign_value': 'utmCampaignValue',
        'utm_source': 'utmSource',
        'utm_medium': 'utmMedium',
        'utm_id': 'utmID',
        'test_sent': 'testSent',
        'header': 'header',
        'footer': 'footer',
        'sender': 'sender',
        'reply_to': 'replyTo',
        'to_field': 'toField',
        'html_content': 'htmlContent',
        'share_link': 'shareLink',
        'tag': 'tag',
        'created_at': 'createdAt',
        'modified_at': 'modifiedAt',
        'inline_image_activation': 'inlineImageActivation',
        'mirror_active': 'mirrorActive',
        'recurring': 'recurring',
        'sent_date': 'sentDate',
        'return_bounce': 'returnBounce'
    }

    def __init__(self, id=None, name=None, subject=None, preview_text=None, type=None, status=None, scheduled_at=None, ab_testing=None, subject_a=None, subject_b=None, split_rule=None, winner_criteria=None, winner_delay=None, send_at_best_time=None, utm_campaign_value=None, utm_source=None, utm_medium=None, utm_id=None, test_sent=None, header=None, footer=None, sender=None, reply_to=None, to_field=None, html_content=None, share_link=None, tag=None, created_at=None, modified_at=None, inline_image_activation=None, mirror_active=None, recurring=None, sent_date=None, return_bounce=None):  # noqa: E501
        """GetExtendedCampaignOverview - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._subject = None
        self._preview_text = None
        self._type = None
        self._status = None
        self._scheduled_at = None
        self._ab_testing = None
        self._subject_a = None
        self._subject_b = None
        self._split_rule = None
        self._winner_criteria = None
        self._winner_delay = None
        self._send_at_best_time = None
        self._utm_campaign_value = None
        self._utm_source = None
        self._utm_medium = None
        self._utm_id = None
        self._test_sent = None
        self._header = None
        self._footer = None
        self._sender = None
        self._reply_to = None
        self._to_field = None
        self._html_content = None
        self._share_link = None
        self._tag = None
        self._created_at = None
        self._modified_at = None
        self._inline_image_activation = None
        self._mirror_active = None
        self._recurring = None
        self._sent_date = None
        self._return_bounce = None
        self.discriminator = None

        self.id = id
        self.name = name
        if subject is not None:
            self.subject = subject
        if preview_text is not None:
            self.preview_text = preview_text
        self.type = type
        self.status = status
        if scheduled_at is not None:
            self.scheduled_at = scheduled_at
        if ab_testing is not None:
            self.ab_testing = ab_testing
        if subject_a is not None:
            self.subject_a = subject_a
        if subject_b is not None:
            self.subject_b = subject_b
        if split_rule is not None:
            self.split_rule = split_rule
        if winner_criteria is not None:
            self.winner_criteria = winner_criteria
        if winner_delay is not None:
            self.winner_delay = winner_delay
        if send_at_best_time is not None:
            self.send_at_best_time = send_at_best_time
        if utm_campaign_value is not None:
            self.utm_campaign_value = utm_campaign_value
        if utm_source is not None:
            self.utm_source = utm_source
        if utm_medium is not None:
            self.utm_medium = utm_medium
        if utm_id is not None:
            self.utm_id = utm_id
        self.test_sent = test_sent
        self.header = header
        self.footer = footer
        self.sender = sender
        self.reply_to = reply_to
        if to_field is not None:
            self.to_field = to_field
        self.html_content = html_content
        if share_link is not None:
            self.share_link = share_link
        if tag is not None:
            self.tag = tag
        self.created_at = created_at
        self.modified_at = modified_at
        if inline_image_activation is not None:
            self.inline_image_activation = inline_image_activation
        if mirror_active is not None:
            self.mirror_active = mirror_active
        if recurring is not None:
            self.recurring = recurring
        if sent_date is not None:
            self.sent_date = sent_date
        if return_bounce is not None:
            self.return_bounce = return_bounce

    @property
    def id(self):
        """Gets the id of this GetExtendedCampaignOverview.  # noqa: E501

        ID of the campaign  # noqa: E501

        :return: The id of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetExtendedCampaignOverview.

        ID of the campaign  # noqa: E501

        :param id: The id of this GetExtendedCampaignOverview.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetExtendedCampaignOverview.  # noqa: E501

        Name of the campaign  # noqa: E501

        :return: The name of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetExtendedCampaignOverview.

        Name of the campaign  # noqa: E501

        :param name: The name of this GetExtendedCampaignOverview.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def subject(self):
        """Gets the subject of this GetExtendedCampaignOverview.  # noqa: E501

        Subject of the campaign. Only available if `abTesting` flag of the campaign is `false`  # noqa: E501

        :return: The subject of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this GetExtendedCampaignOverview.

        Subject of the campaign. Only available if `abTesting` flag of the campaign is `false`  # noqa: E501

        :param subject: The subject of this GetExtendedCampaignOverview.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def preview_text(self):
        """Gets the preview_text of this GetExtendedCampaignOverview.  # noqa: E501

        Preview text or preheader of the email campaign  # noqa: E501

        :return: The preview_text of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._preview_text

    @preview_text.setter
    def preview_text(self, preview_text):
        """Sets the preview_text of this GetExtendedCampaignOverview.

        Preview text or preheader of the email campaign  # noqa: E501

        :param preview_text: The preview_text of this GetExtendedCampaignOverview.  # noqa: E501
        :type: str
        """

        self._preview_text = preview_text

    @property
    def type(self):
        """Gets the type of this GetExtendedCampaignOverview.  # noqa: E501

        Type of campaign  # noqa: E501

        :return: The type of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetExtendedCampaignOverview.

        Type of campaign  # noqa: E501

        :param type: The type of this GetExtendedCampaignOverview.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["classic", "trigger"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def status(self):
        """Gets the status of this GetExtendedCampaignOverview.  # noqa: E501

        Status of the campaign  # noqa: E501

        :return: The status of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetExtendedCampaignOverview.

        Status of the campaign  # noqa: E501

        :param status: The status of this GetExtendedCampaignOverview.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["draft", "sent", "archive", "queued", "suspended", "in_process"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def scheduled_at(self):
        """Gets the scheduled_at of this GetExtendedCampaignOverview.  # noqa: E501

        UTC date-time on which campaign is scheduled (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501

        :return: The scheduled_at of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._scheduled_at

    @scheduled_at.setter
    def scheduled_at(self, scheduled_at):
        """Sets the scheduled_at of this GetExtendedCampaignOverview.

        UTC date-time on which campaign is scheduled (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501

        :param scheduled_at: The scheduled_at of this GetExtendedCampaignOverview.  # noqa: E501
        :type: str
        """

        self._scheduled_at = scheduled_at

    @property
    def ab_testing(self):
        """Gets the ab_testing of this GetExtendedCampaignOverview.  # noqa: E501

        Status of A/B Test for the campaign. abTesting = false means it is disabled, & abTesting = true means it is enabled.  # noqa: E501

        :return: The ab_testing of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: bool
        """
        return self._ab_testing

    @ab_testing.setter
    def ab_testing(self, ab_testing):
        """Sets the ab_testing of this GetExtendedCampaignOverview.

        Status of A/B Test for the campaign. abTesting = false means it is disabled, & abTesting = true means it is enabled.  # noqa: E501

        :param ab_testing: The ab_testing of this GetExtendedCampaignOverview.  # noqa: E501
        :type: bool
        """

        self._ab_testing = ab_testing

    @property
    def subject_a(self):
        """Gets the subject_a of this GetExtendedCampaignOverview.  # noqa: E501

        Subject A of the ab-test campaign. Only available if `abTesting` flag of the campaign is `true`  # noqa: E501

        :return: The subject_a of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._subject_a

    @subject_a.setter
    def subject_a(self, subject_a):
        """Sets the subject_a of this GetExtendedCampaignOverview.

        Subject A of the ab-test campaign. Only available if `abTesting` flag of the campaign is `true`  # noqa: E501

        :param subject_a: The subject_a of this GetExtendedCampaignOverview.  # noqa: E501
        :type: str
        """

        self._subject_a = subject_a

    @property
    def subject_b(self):
        """Gets the subject_b of this GetExtendedCampaignOverview.  # noqa: E501

        Subject B of the ab-test campaign. Only available if `abTesting` flag of the campaign is `true`  # noqa: E501

        :return: The subject_b of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._subject_b

    @subject_b.setter
    def subject_b(self, subject_b):
        """Sets the subject_b of this GetExtendedCampaignOverview.

        Subject B of the ab-test campaign. Only available if `abTesting` flag of the campaign is `true`  # noqa: E501

        :param subject_b: The subject_b of this GetExtendedCampaignOverview.  # noqa: E501
        :type: str
        """

        self._subject_b = subject_b

    @property
    def split_rule(self):
        """Gets the split_rule of this GetExtendedCampaignOverview.  # noqa: E501

        The size of your ab-test groups. Only available if `abTesting` flag of the campaign is `true`  # noqa: E501

        :return: The split_rule of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: int
        """
        return self._split_rule

    @split_rule.setter
    def split_rule(self, split_rule):
        """Sets the split_rule of this GetExtendedCampaignOverview.

        The size of your ab-test groups. Only available if `abTesting` flag of the campaign is `true`  # noqa: E501

        :param split_rule: The split_rule of this GetExtendedCampaignOverview.  # noqa: E501
        :type: int
        """

        self._split_rule = split_rule

    @property
    def winner_criteria(self):
        """Gets the winner_criteria of this GetExtendedCampaignOverview.  # noqa: E501

        Criteria for the winning version. Only available if `abTesting` flag of the campaign is `true`  # noqa: E501

        :return: The winner_criteria of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._winner_criteria

    @winner_criteria.setter
    def winner_criteria(self, winner_criteria):
        """Sets the winner_criteria of this GetExtendedCampaignOverview.

        Criteria for the winning version. Only available if `abTesting` flag of the campaign is `true`  # noqa: E501

        :param winner_criteria: The winner_criteria of this GetExtendedCampaignOverview.  # noqa: E501
        :type: str
        """

        self._winner_criteria = winner_criteria

    @property
    def winner_delay(self):
        """Gets the winner_delay of this GetExtendedCampaignOverview.  # noqa: E501

        The duration of the test in hours at the end of which the winning version will be sent. Only available if `abTesting` flag of the campaign is `true`  # noqa: E501

        :return: The winner_delay of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: int
        """
        return self._winner_delay

    @winner_delay.setter
    def winner_delay(self, winner_delay):
        """Sets the winner_delay of this GetExtendedCampaignOverview.

        The duration of the test in hours at the end of which the winning version will be sent. Only available if `abTesting` flag of the campaign is `true`  # noqa: E501

        :param winner_delay: The winner_delay of this GetExtendedCampaignOverview.  # noqa: E501
        :type: int
        """

        self._winner_delay = winner_delay

    @property
    def send_at_best_time(self):
        """Gets the send_at_best_time of this GetExtendedCampaignOverview.  # noqa: E501

        It is true if you have chosen to send your campaign at best time, otherwise it is false  # noqa: E501

        :return: The send_at_best_time of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: bool
        """
        return self._send_at_best_time

    @send_at_best_time.setter
    def send_at_best_time(self, send_at_best_time):
        """Sets the send_at_best_time of this GetExtendedCampaignOverview.

        It is true if you have chosen to send your campaign at best time, otherwise it is false  # noqa: E501

        :param send_at_best_time: The send_at_best_time of this GetExtendedCampaignOverview.  # noqa: E501
        :type: bool
        """

        self._send_at_best_time = send_at_best_time

    @property
    def utm_campaign_value(self):
        """Gets the utm_campaign_value of this GetExtendedCampaignOverview.  # noqa: E501

        utm parameter associated with campaign  # noqa: E501

        :return: The utm_campaign_value of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._utm_campaign_value

    @utm_campaign_value.setter
    def utm_campaign_value(self, utm_campaign_value):
        """Sets the utm_campaign_value of this GetExtendedCampaignOverview.

        utm parameter associated with campaign  # noqa: E501

        :param utm_campaign_value: The utm_campaign_value of this GetExtendedCampaignOverview.  # noqa: E501
        :type: str
        """

        self._utm_campaign_value = utm_campaign_value

    @property
    def utm_source(self):
        """Gets the utm_source of this GetExtendedCampaignOverview.  # noqa: E501

        source of utm parameter  # noqa: E501

        :return: The utm_source of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._utm_source

    @utm_source.setter
    def utm_source(self, utm_source):
        """Sets the utm_source of this GetExtendedCampaignOverview.

        source of utm parameter  # noqa: E501

        :param utm_source: The utm_source of this GetExtendedCampaignOverview.  # noqa: E501
        :type: str
        """

        self._utm_source = utm_source

    @property
    def utm_medium(self):
        """Gets the utm_medium of this GetExtendedCampaignOverview.  # noqa: E501

        medium parameter  # noqa: E501

        :return: The utm_medium of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._utm_medium

    @utm_medium.setter
    def utm_medium(self, utm_medium):
        """Sets the utm_medium of this GetExtendedCampaignOverview.

        medium parameter  # noqa: E501

        :param utm_medium: The utm_medium of this GetExtendedCampaignOverview.  # noqa: E501
        :type: str
        """

        self._utm_medium = utm_medium

    @property
    def utm_id(self):
        """Gets the utm_id of this GetExtendedCampaignOverview.  # noqa: E501

        utm id  # noqa: E501

        :return: The utm_id of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: int
        """
        return self._utm_id

    @utm_id.setter
    def utm_id(self, utm_id):
        """Sets the utm_id of this GetExtendedCampaignOverview.

        utm id  # noqa: E501

        :param utm_id: The utm_id of this GetExtendedCampaignOverview.  # noqa: E501
        :type: int
        """

        self._utm_id = utm_id

    @property
    def test_sent(self):
        """Gets the test_sent of this GetExtendedCampaignOverview.  # noqa: E501

        Retrieved the status of test email sending. (true=Test email has been sent  false=Test email has not been sent)  # noqa: E501

        :return: The test_sent of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: bool
        """
        return self._test_sent

    @test_sent.setter
    def test_sent(self, test_sent):
        """Sets the test_sent of this GetExtendedCampaignOverview.

        Retrieved the status of test email sending. (true=Test email has been sent  false=Test email has not been sent)  # noqa: E501

        :param test_sent: The test_sent of this GetExtendedCampaignOverview.  # noqa: E501
        :type: bool
        """
        if test_sent is None:
            raise ValueError("Invalid value for `test_sent`, must not be `None`")  # noqa: E501

        self._test_sent = test_sent

    @property
    def header(self):
        """Gets the header of this GetExtendedCampaignOverview.  # noqa: E501

        Header of the campaign  # noqa: E501

        :return: The header of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this GetExtendedCampaignOverview.

        Header of the campaign  # noqa: E501

        :param header: The header of this GetExtendedCampaignOverview.  # noqa: E501
        :type: str
        """
        if header is None:
            raise ValueError("Invalid value for `header`, must not be `None`")  # noqa: E501

        self._header = header

    @property
    def footer(self):
        """Gets the footer of this GetExtendedCampaignOverview.  # noqa: E501

        Footer of the campaign  # noqa: E501

        :return: The footer of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._footer

    @footer.setter
    def footer(self, footer):
        """Sets the footer of this GetExtendedCampaignOverview.

        Footer of the campaign  # noqa: E501

        :param footer: The footer of this GetExtendedCampaignOverview.  # noqa: E501
        :type: str
        """
        if footer is None:
            raise ValueError("Invalid value for `footer`, must not be `None`")  # noqa: E501

        self._footer = footer

    @property
    def sender(self):
        """Gets the sender of this GetExtendedCampaignOverview.  # noqa: E501


        :return: The sender of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: GetExtendedCampaignOverviewSender
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this GetExtendedCampaignOverview.


        :param sender: The sender of this GetExtendedCampaignOverview.  # noqa: E501
        :type: GetExtendedCampaignOverviewSender
        """
        if sender is None:
            raise ValueError("Invalid value for `sender`, must not be `None`")  # noqa: E501

        self._sender = sender

    @property
    def reply_to(self):
        """Gets the reply_to of this GetExtendedCampaignOverview.  # noqa: E501

        Email defined as the \"Reply to\" of the campaign  # noqa: E501

        :return: The reply_to of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """Sets the reply_to of this GetExtendedCampaignOverview.

        Email defined as the \"Reply to\" of the campaign  # noqa: E501

        :param reply_to: The reply_to of this GetExtendedCampaignOverview.  # noqa: E501
        :type: str
        """
        if reply_to is None:
            raise ValueError("Invalid value for `reply_to`, must not be `None`")  # noqa: E501

        self._reply_to = reply_to

    @property
    def to_field(self):
        """Gets the to_field of this GetExtendedCampaignOverview.  # noqa: E501

        Customisation of the \"to\" field of the campaign  # noqa: E501

        :return: The to_field of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._to_field

    @to_field.setter
    def to_field(self, to_field):
        """Sets the to_field of this GetExtendedCampaignOverview.

        Customisation of the \"to\" field of the campaign  # noqa: E501

        :param to_field: The to_field of this GetExtendedCampaignOverview.  # noqa: E501
        :type: str
        """

        self._to_field = to_field

    @property
    def html_content(self):
        """Gets the html_content of this GetExtendedCampaignOverview.  # noqa: E501

        HTML content of the campaign  # noqa: E501

        :return: The html_content of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._html_content

    @html_content.setter
    def html_content(self, html_content):
        """Sets the html_content of this GetExtendedCampaignOverview.

        HTML content of the campaign  # noqa: E501

        :param html_content: The html_content of this GetExtendedCampaignOverview.  # noqa: E501
        :type: str
        """
        if html_content is None:
            raise ValueError("Invalid value for `html_content`, must not be `None`")  # noqa: E501

        self._html_content = html_content

    @property
    def share_link(self):
        """Gets the share_link of this GetExtendedCampaignOverview.  # noqa: E501

        Link to share the campaign on social medias  # noqa: E501

        :return: The share_link of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._share_link

    @share_link.setter
    def share_link(self, share_link):
        """Sets the share_link of this GetExtendedCampaignOverview.

        Link to share the campaign on social medias  # noqa: E501

        :param share_link: The share_link of this GetExtendedCampaignOverview.  # noqa: E501
        :type: str
        """

        self._share_link = share_link

    @property
    def tag(self):
        """Gets the tag of this GetExtendedCampaignOverview.  # noqa: E501

        Tag of the campaign  # noqa: E501

        :return: The tag of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this GetExtendedCampaignOverview.

        Tag of the campaign  # noqa: E501

        :param tag: The tag of this GetExtendedCampaignOverview.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def created_at(self):
        """Gets the created_at of this GetExtendedCampaignOverview.  # noqa: E501

        Creation UTC date-time of the campaign (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501

        :return: The created_at of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GetExtendedCampaignOverview.

        Creation UTC date-time of the campaign (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501

        :param created_at: The created_at of this GetExtendedCampaignOverview.  # noqa: E501
        :type: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this GetExtendedCampaignOverview.  # noqa: E501

        UTC date-time of last modification of the campaign (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501

        :return: The modified_at of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this GetExtendedCampaignOverview.

        UTC date-time of last modification of the campaign (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501

        :param modified_at: The modified_at of this GetExtendedCampaignOverview.  # noqa: E501
        :type: str
        """
        if modified_at is None:
            raise ValueError("Invalid value for `modified_at`, must not be `None`")  # noqa: E501

        self._modified_at = modified_at

    @property
    def inline_image_activation(self):
        """Gets the inline_image_activation of this GetExtendedCampaignOverview.  # noqa: E501

        Status of inline image. inlineImageActivation = false means image can’t be embedded, & inlineImageActivation = true means image can be embedded, in the email.  # noqa: E501

        :return: The inline_image_activation of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: bool
        """
        return self._inline_image_activation

    @inline_image_activation.setter
    def inline_image_activation(self, inline_image_activation):
        """Sets the inline_image_activation of this GetExtendedCampaignOverview.

        Status of inline image. inlineImageActivation = false means image can’t be embedded, & inlineImageActivation = true means image can be embedded, in the email.  # noqa: E501

        :param inline_image_activation: The inline_image_activation of this GetExtendedCampaignOverview.  # noqa: E501
        :type: bool
        """

        self._inline_image_activation = inline_image_activation

    @property
    def mirror_active(self):
        """Gets the mirror_active of this GetExtendedCampaignOverview.  # noqa: E501

        Status of mirror links in campaign. mirrorActive = false means mirror links are deactivated, & mirrorActive = true means mirror links are activated, in the campaign  # noqa: E501

        :return: The mirror_active of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: bool
        """
        return self._mirror_active

    @mirror_active.setter
    def mirror_active(self, mirror_active):
        """Sets the mirror_active of this GetExtendedCampaignOverview.

        Status of mirror links in campaign. mirrorActive = false means mirror links are deactivated, & mirrorActive = true means mirror links are activated, in the campaign  # noqa: E501

        :param mirror_active: The mirror_active of this GetExtendedCampaignOverview.  # noqa: E501
        :type: bool
        """

        self._mirror_active = mirror_active

    @property
    def recurring(self):
        """Gets the recurring of this GetExtendedCampaignOverview.  # noqa: E501

        FOR TRIGGER ONLY ! Type of trigger campaign.recurring = false means contact can receive the same Trigger campaign only once, & recurring = true means contact can receive the same Trigger campaign several times  # noqa: E501

        :return: The recurring of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: bool
        """
        return self._recurring

    @recurring.setter
    def recurring(self, recurring):
        """Sets the recurring of this GetExtendedCampaignOverview.

        FOR TRIGGER ONLY ! Type of trigger campaign.recurring = false means contact can receive the same Trigger campaign only once, & recurring = true means contact can receive the same Trigger campaign several times  # noqa: E501

        :param recurring: The recurring of this GetExtendedCampaignOverview.  # noqa: E501
        :type: bool
        """

        self._recurring = recurring

    @property
    def sent_date(self):
        """Gets the sent_date of this GetExtendedCampaignOverview.  # noqa: E501

        Sent UTC date-time of the campaign (YYYY-MM-DDTHH:mm:ss.SSSZ). Only available if 'status' of the campaign is 'sent'  # noqa: E501

        :return: The sent_date of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._sent_date

    @sent_date.setter
    def sent_date(self, sent_date):
        """Sets the sent_date of this GetExtendedCampaignOverview.

        Sent UTC date-time of the campaign (YYYY-MM-DDTHH:mm:ss.SSSZ). Only available if 'status' of the campaign is 'sent'  # noqa: E501

        :param sent_date: The sent_date of this GetExtendedCampaignOverview.  # noqa: E501
        :type: str
        """

        self._sent_date = sent_date

    @property
    def return_bounce(self):
        """Gets the return_bounce of this GetExtendedCampaignOverview.  # noqa: E501

        Total number of non-delivered campaigns for a particular campaign id.  # noqa: E501

        :return: The return_bounce of this GetExtendedCampaignOverview.  # noqa: E501
        :rtype: int
        """
        return self._return_bounce

    @return_bounce.setter
    def return_bounce(self, return_bounce):
        """Sets the return_bounce of this GetExtendedCampaignOverview.

        Total number of non-delivered campaigns for a particular campaign id.  # noqa: E501

        :param return_bounce: The return_bounce of this GetExtendedCampaignOverview.  # noqa: E501
        :type: int
        """

        self._return_bounce = return_bounce

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GetExtendedCampaignOverview, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetExtendedCampaignOverview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
