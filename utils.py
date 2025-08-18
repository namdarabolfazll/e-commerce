from kavenegar import *
def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('337872662F65484F716E324C2B6877374F443677346F4E73675262575666336442446453662B53397858633D')
        params = {
            'sender': '',  # optional
            'receptor':phone_number,  # multiple mobile number, split by comma
            'message': f'this is your code :{code}',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


