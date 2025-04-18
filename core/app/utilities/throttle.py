from rest_framework.throttling import SimpleRateThrottle


class OTPAutherizationThrottle(SimpleRateThrottle):
    scope = "otp-authorization"

    def get_cache_key(self, request, view):
        ident = self.get_ident(request)
        return f"{self.scope}:{ident}"


class OTPVerifcationThrottle(SimpleRateThrottle):
    scope = "otp-verification"

    def get_cache_key(self, request, view):
        ident = self.get_ident(request)
        return f"{self.scope}:{ident}"
