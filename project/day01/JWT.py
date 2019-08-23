import copy
import json
import base64
import hmac
import time


class Jwt:
    def __init__(self):
        pass

    @staticmethod
    def encode(payload, key, exp=300):
        header = {'alg': "HS256", 'typ': 'JWT'}
        header_json = json.dumps(header, sort_keys=True, separators=(',', ':'))
        # 生成base64加密串
        header_base64 = Jwt.b64encode(header_json.encode())

        # 参数中的payload{'username': 'xiaojian'}
        payload = copy.deepcopy(payload)
        # 添加共有声明  -  exp
        payload['exp'] = int(time.time()) + exp
        payload_json = json.dumps(payload, sort_keys=True, separators=(',', ':'))
        payload_base64 = Jwt.b64encode(payload_json.encode())

        signature = header_base64 + b"." + payload_base64
        if isinstance(key, str):
            key = key.encode()
        hm = hmac.new(key, signature, digestmod='SHA256')
        h_base64 = Jwt.b64encode(hm.digest())
        return header_base64 + b"." + payload_base64 + b"." + h_base64

    @staticmethod
    def b64encode(j_s):

        return base64.urlsafe_b64encode(j_s).replace(b'=', b'')

    @staticmethod
    def b64decode(b64_s):

        rem = len(b64_s) % 4
        if rem > 0:
            b64_s += b"=" * (4 - rem)
        return base64 .urlsafe_b64decode(b64_s)

    @staticmethod
    def decode(token, key):
        header_b, payload_b, sign_b = token.split(b".")
        if isinstance(key, str):
            key = key.encode()

        hm = hmac.new(key, header_b + b"." + payload_b, digestmod='SHA256')
        if sign_b != Jwt.b64encode(hm.digest()):
            raise JwtSignError('----The sign is error!!!')
        payload_json = Jwt.b64decode(payload_b)
        payload = json.loads(payload_json.decode())

        exp = payload['exp']
        now = time.time()
        if now > exp:
            raise JwtExpireError('-----The token is expire!!!')

        return payload


class JwtSignError(Exception):
    def __init__(self, error_msg):
        self.error_msg = error_msg

    def __str__(self):
        return '<JwtSignError is %s>' % self.error_msg


class JwtExpireError(Exception):
    def __init__(self, error_msg):
        self.error_msg = error_msg

    def __str__(self):
        return '<JwtExpireError is %s>' % self.error_msg


if __name__ == "__main__":
    s = Jwt.encode({'username': 'xiaojian'}, "123", exp=300)
    print(Jwt.decode(s, "123"))
