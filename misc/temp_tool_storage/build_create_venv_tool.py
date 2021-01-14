import os
import shutil
import base64
from collections import namedtuple

import argparse
PROJECT_NAME_PLACEHOLDER = "-PLEASE_SET_THIS-"
FILE_TUPLE = namedtuple('FileTuple', ['name', 'path', 'typus', 'bin_content'])


CREATE_VENV__CMD = b'UkVNIE5lY2Vzc2FyeSBGaWxlczoNClJFTSAtIHByZV9zZXR1cF9zY3JpcHRzLnR4dA0KUkVNIC0gcmVxdWlyZWRfcGVyc29uYWxfcGFja2FnZXMudHh0DQpSRU0gLSByZXF1aXJlZF9taXNjLnR4dA0KUkVNIC0gcmVxdWlyZWRfUXQudHh0DQpSRU0gLSByZXF1aXJlZF9mcm9tX2dpdGh1Yi50eHQNClJFTSAtIHJlcXVpcmVkX3Rlc3QudHh0DQpSRU0gLSByZXF1aXJlZF9kZXYudHh0DQpSRU0gLSBwb3N0X3NldHVwX3NjcmlwdHMudHh0DQpSRU0gLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQ0KDQpARUNITyBPRkYNClNFVExPQ0FMIEVOQUJMRUVYVEVOU0lPTlMNCg0KDQoNCg0KU0VUIFBST0pFQ1RfTkFNRT0tUExFQVNFX1NFVF9USElTLQ0KDQpTRVQgT0xESE9NRV9GT0xERVI9JX5kcDANCg0KUkVNIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQ0KU0VUIF9kYXRlPSVEQVRFOi89LSUNClNFVCBfdGltZT0lVElNRTo6PSUNClNFVCBfdGltZT0lX3RpbWU6ID0wJQ0KUkVNIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQ0KUkVNIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQ0KU0VUIF9kZWNhZGVzPSVfZGF0ZTp+LTIlDQpTRVQgX3llYXJzPSVfZGF0ZTp+LTQlDQpTRVQgX21vbnRocz0lX2RhdGU6fjMsMiUNClNFVCBfZGF5cz0lX2RhdGU6fjAsMiUNClJFTSAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0NClNFVCBfaG91cnM9JV90aW1lOn4wLDIlDQpTRVQgX21pbnV0ZXM9JV90aW1lOn4yLDIlDQpTRVQgX3NlY29uZHM9JV90aW1lOn40LDIlDQpSRU0gLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tDQpTRVQgVElNRUJMT0NLPSVfeWVhcnMlLSVfbW9udGhzJS0lX2RheXMlXyVfaG91cnMlLSVfbWludXRlcyUtJV9zZWNvbmRzJQ0KDQpFQ0hPICoqKioqKioqKioqKioqKioqIEN1cnJlbnQgdGltZSBpcyAqKioqKioqKioqKioqKioqKg0KRUNITyAgICAgICAgICAgICAgICAgICAgICVUSU1FQkxPQ0slDQoNCkVDSE8gIyMjIyMjIyMjIyMjIyMjIyMgY2hhbmdpbmcgZGlyZWN0b3J5IHRvICVPTERIT01FX0ZPTERFUiUNCkNEICVPTERIT01FX0ZPTERFUiUNCkVDSE8uDQoNCkVDSE8gLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0gUFJFLVNFVFVQIFNDUklQVFMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0NCkVDSE8uDQpGT1IgL0YgInRva2Vucz0xLDIgZGVsaW1zPSwiICUlQSBpbiAoLlx2ZW52X3NldHVwX3NldHRpbmdzXHByZV9zZXR1cF9zY3JpcHRzLnR4dCkgZG8gKA0KRUNITy4NCkVDSE8gLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0gQ2FsbGluZyAlJUEgd2l0aCAlJUIgLS0tLS0tLS0tLS0tLS1ePg0KQ0FMTCAlJUEgJSVCDQpFQ0hPLg0KKQ0KDQoNCg0KRUNITyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSBCQVNJQyBWRU5WIFNFVFVQIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tDQpFQ0hPLg0KDQpFQ0hPICMjIyMjIyMjIyMjIyMjIyMjIHN1c3BlbmRpbmcgRHJvcGJveA0KQ0FMTCBwc2tpbGw2NCBEcm9wYm94DQpFQ0hPLg0KDQpFQ0hPICMjIyMjIyMjIyMjIyMjIyMjIFJlbW92aW5nIG9sZCB2ZW52IGZvbGRlcg0KUkQgL1MgL1EgLi5cLnZlbnYNCkVDSE8uDQoNCkVDSE8gIyMjIyMjIyMjIyMjIyMjIyMgY3JlYXRpbmcgbmV3IHZlbnYgZm9sZGVyDQpta2RpciAuLlwudmVudg0KRUNITy4NCg0KRUNITyAjIyMjIyMjIyMjIyMjIyMjIyBDYWxsaW5nIHZlbnYgbW9kdWxlIHRvIGluaXRpYWxpemUgbmV3IHZlbnYNCnB5dGhvbiAtbSB2ZW52IC4uXC52ZW52DQpFQ0hPLg0KDQpFQ0hPICMjIyMjIyMjIyMjIyMjIyMjIGNoYW5naW5nIGRpcmVjdG9yeSB0byAuLlwudmVudg0KQ0QgLi5cLnZlbnYNCkVDSE8uDQoNCkVDSE8gIyMjIyMjIyMjIyMjIyMjIyMgYWN0aXZhdGluZyB2ZW52IGZvciBwYWNrYWdlIGluc3RhbGxhdGlvbg0KQ0FMTCAuXFNjcmlwdHNcYWN0aXZhdGUuYmF0DQpFQ0hPLg0KDQpFQ0hPICMjIyMjIyMjIyMjIyMjIyMjIHVwZ3JhZGluZyBwaXAgdG8gZ2V0IHJpZCBvZiBzdHVwaWQgd2FybmluZw0KQ0FMTCAlT0xESE9NRV9GT0xERVIlZ2V0LXBpcC5weQ0KRUNITy4NCg0KRUNITy4NCkVDSE8gLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQ0KRUNITyArKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKyBJTlNUQUxMSU5HIFBBQ0tBR0VTICsrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrDQpFQ0hPIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0NCkVDSE8uDQpFQ0hPLg0KDQpDRCAlT0xESE9NRV9GT0xERVIlDQoNCkVDSE8gKysrKysrKysrKysrKysrKysrKysrKysrKysrKysgU3RhbmRhcmQgUGFja2FnZXMgKysrKysrKysrKysrKysrKysrKysrKysrKysrKysNCkVDSE8uDQpFQ0hPLg0KDQpFQ0hPICMjIyMjIyMjIyMjIyMjIyMjIEluc3RhbGxpbmcgU2V0dXB0b29scw0KQ0FMTCBwaXAgaW5zdGFsbCAtLXVwZ3JhZGUgLS1wcmUgc2V0dXB0b29scw0KRUNITy4NCg0KRUNITyAjIyMjIyMjIyMjIyMjIyMjIyBJbnN0YWxsaW5nIHdoZWVsDQpDQUxMIHBpcCBpbnN0YWxsIC0tdXBncmFkZSAtLXByZSB3aGVlbA0KRUNITy4NCg0KRUNITyAjIyMjIyMjIyMjIyMjIyMjIyBJbnN0YWxsaW5nIHB5dGhvbi1kb3RlbnYNCkNBTEwgcGlwIGluc3RhbGwgLS11cGdyYWRlIC0tcHJlIHB5dGhvbi1kb3RlbnYNCkVDSE8uDQoNCg0KDQpFQ0hPICMjIyMjIyMjIyMjIyMjIyMjIEluc3RhbGxpbmcgZmxpdA0KQ0FMTCBwaXAgaW5zdGFsbCAtLWZvcmNlLXJlaW5zdGFsbCAtLW5vLWNhY2hlLWRpciAtLXVwZ3JhZGUgLS1wcmUgZmxpdA0KRUNITy4NCg0KRUNITy4NCkVDSE8uDQoNCkVDSE8gKysrKysrKysrKysrKysrKysrKysrKysrKysrKysgR2lkIFBhY2thZ2VzICsrKysrKysrKysrKysrKysrKysrKysrKysrKysrDQpFQ0hPLg0KRUNITy4NCg0KRk9SIC9GICJ0b2tlbnM9MSwyIGRlbGltcz0sIiAlJUEgaW4gKC5cdmVudl9zZXR1cF9zZXR0aW5nc1xyZXF1aXJlZF9wZXJzb25hbF9wYWNrYWdlcy50eHQpIGRvICgNCkVDSE8uDQpFQ0hPIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tIEluc3RhbGxpbmcgJSVCIC0tLS0tLS0tLS0tLS0tXj4NCkVDSE8uDQpQVVNIRCAlJUENCkNBTEwgZmxpdCBpbnN0YWxsIC1zDQpQT1BEDQpFQ0hPLg0KKQ0KDQpFQ0hPLg0KRUNITy4NCg0KRWNobyArKysrKysrKysrKysrKysrKysrKysrKysrKysrKyBNaXNjIFBhY2thZ2VzICsrKysrKysrKysrKysrKysrKysrKysrKysrKysrDQpFQ0hPLg0KRk9SIC9GICJ0b2tlbnM9MSBkZWxpbXM9LCIgJSVBIGluICguXHZlbnZfc2V0dXBfc2V0dGluZ3NccmVxdWlyZWRfbWlzYy50eHQpIGRvICgNCkVDSE8uDQpFQ0hPIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tIEluc3RhbGxpbmcgJSVBIC0tLS0tLS0tLS0tLS0tXj4NCkVDSE8uDQpDQUxMIHBpcCBpbnN0YWxsIC0tdXBncmFkZSAlJUENCkVDSE8uDQopDQoNCkVDSE8uDQpFQ0hPLg0KDQpFY2hvICsrKysrKysrKysrKysrKysrKysrKysrKysrKysrIFF0IFBhY2thZ2VzICsrKysrKysrKysrKysrKysrKysrKysrKysrKysrDQpFQ0hPLg0KRk9SIC9GICJ0b2tlbnM9MSBkZWxpbXM9LCIgJSVBIGluICguXHZlbnZfc2V0dXBfc2V0dGluZ3NccmVxdWlyZWRfUXQudHh0KSBkbyAoDQpFQ0hPLg0KRUNITyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSBJbnN0YWxsaW5nICUlQSAtLS0tLS0tLS0tLS0tLV4+DQpFQ0hPLg0KQ0FMTCBwaXAgaW5zdGFsbCAtLXVwZ3JhZGUgJSVBDQpFQ0hPLg0KKQ0KDQpFQ0hPLg0KRUNITy4NCg0KRWNobyArKysrKysrKysrKysrKysrKysrKysrKysrKysrKyBQYWNrYWdlcyBGcm9tIEdpdGh1YiArKysrKysrKysrKysrKysrKysrKysrKysrKysrKw0KRUNITy4NCkZPUiAvRiAidG9rZW5zPTEgZGVsaW1zPSwiICUlQSBpbiAoLlx2ZW52X3NldHVwX3NldHRpbmdzXHJlcXVpcmVkX2Zyb21fZ2l0aHViLnR4dCkgZG8gKA0KRUNITy4NCkVDSE8gLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0gSW5zdGFsbGluZyAlJUEgLS0tLS0tLS0tLS0tLS1ePg0KRUNITy4NCkNBTEwgY2FsbCBwaXAgaW5zdGFsbCAtLXVwZ3JhZGUgZ2l0KyUlQQ0KRUNITy4NCikNCg0KRUNITy4NCkVDSE8uDQoNCkVjaG8gKysrKysrKysrKysrKysrKysrKysrKysrKysrKysgVGVzdCBQYWNrYWdlcyArKysrKysrKysrKysrKysrKysrKysrKysrKysrKw0KRUNITy4NCkZPUiAvRiAidG9rZW5zPTEgZGVsaW1zPSwiICUlQSBpbiAoLlx2ZW52X3NldHVwX3NldHRpbmdzXHJlcXVpcmVkX3Rlc3QudHh0KSBkbyAoDQpFQ0hPLg0KRUNITyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSBJbnN0YWxsaW5nICUlQSAtLS0tLS0tLS0tLS0tLV4+DQpFQ0hPLg0KQ0FMTCBwaXAgaW5zdGFsbCAtLXVwZ3JhZGUgJSVBDQpFQ0hPLg0KKQ0KDQpFQ0hPLg0KRUNITy4NCg0KRWNobyArKysrKysrKysrKysrKysrKysrKysrKysrKysrKyBEZXYgUGFja2FnZXMgKysrKysrKysrKysrKysrKysrKysrKysrKysrKysNCkVDSE8uDQpGT1IgL0YgInRva2Vucz0xIGRlbGltcz0sIiAlJUEgaW4gKC5cdmVudl9zZXR1cF9zZXR0aW5nc1xyZXF1aXJlZF9kZXYudHh0KSBkbyAoDQpFQ0hPLg0KRUNITyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSBJbnN0YWxsaW5nICUlQSAtLS0tLS0tLS0tLS0tLV4+DQpFQ0hPLg0KQ0FMTCBwaXAgaW5zdGFsbCAtLW5vLWNhY2hlLWRpciAtLXVwZ3JhZGUgLS1wcmUgJSVBDQpFQ0hPLg0KKQ0KDQpFQ0hPLg0KRUNITy4NCg0KDQpFQ0hPIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tIElOU1RBTEwgVEhFIFBST0pFQ1QgSVRTRUxGIEFTIC1ERVYgUEFDS0FHRSAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQ0KY2QgLi5cDQpyZW0gY2FsbCBwaXAgaW5zdGFsbCAtZSAuDQpjYWxsIGZsaXQgaW5zdGFsbCAtcw0KRUNITy4NCg0KRUNITy4NCkVDSE8uDQoNCkNEICVPTERIT01FX0ZPTERFUiUNCg0KRUNITyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSBQT1NULVNFVFVQIFNDUklQVFMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0NCkVDSE8uDQpGT1IgL0YgInRva2Vucz0xLDIgZGVsaW1zPSwiICUlQSBpbiAoLlx2ZW52X3NldHVwX3NldHRpbmdzXHBvc3Rfc2V0dXBfc2NyaXB0cy50eHQpIGRvICgNCkVDSE8uDQpFQ0hPIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tIENhbGxpbmcgJSVBIHdpdGggJSVCIC0tLS0tLS0tLS0tLS0tXj4NCkNBTEwgJSVBICUlQg0KRUNITy4NCikNCg0KRUNITy4NCkVDSE8uDQoNCkVDSE8uDQpFQ0hPICMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMNCkVDSE8gLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQ0KRUNITyAjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjDQpFQ0hPLg0KRUNITyArKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKyBGSU5JU0hFRCArKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrDQpFQ0hPLg0KRUNITyAjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjDQpFQ0hPIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0NCkVDSE8gIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIw0KRUNITy4='
CREATE_VENV_EXTRA_ENVVARS__PY = b'aW1wb3J0IG9zDQppbXBvcnQgc3lzDQoNCm9zLmNoZGlyKHN5cy5hcmd2WzFdKQ0KUFJPSkVDVF9OQU1FID0gc3lzLmFyZ3ZbMl0NClJFTF9BQ1RJVkFURV9TQ1JJUFRfUEFUSCA9ICcuLi8udmVudi9TY3JpcHRzL2FjdGl2YXRlLmJhdCcNClJFUExBQ0VNRU5UID0gciIiIkBlY2hvIG9mZg0KDQpzZXQgRklMRUZPTERFUj0lfmRwMA0KDQpwdXNoZCAlRklMRUZPTERFUiUNCnJlbSAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tDQpjZCAuLlwuLlx0b29scw0KZWNobyAjIyMjIyMjIyMjIyMjIyMjIyMjIyMgc2V0dGluZyB2YXJzIGZyb20gJWNkJVxfcHJvamVjdF9tZXRhLmVudg0KZm9yIC9mICUlaSBpbiAoX3Byb2plY3RfbWV0YS5lbnYpIGRvIHNldCAlJWkgJiYgZWNobyAlJWkNCnJlbSAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tDQpwb3BkDQoiIiINCg0KDQpkZWYgY3JlYXRlX3Byb2plY3RfbWV0YV9lbnZfZmlsZSgpOg0KICAgIF93b3Jrc3BhY2VkaXJiYXRjaCA9IG9zLmdldGN3ZCgpDQogICAgX3RvcGxldmVsbW9kdWxlID0gb3MucGF0aC5qb2luKF93b3Jrc3BhY2VkaXJiYXRjaCwgUFJPSkVDVF9OQU1FKQ0KICAgIF9tYWluX3NjcmlwdF9maWxlID0gb3MucGF0aC5qb2luKF90b3BsZXZlbG1vZHVsZSwgJ19fbWFpbl9fLnB5JykNCiAgICB3aXRoIG9wZW4oIl9wcm9qZWN0X21ldGEuZW52IiwgJ3cnKSBhcyBlbnZmaWxlOg0KICAgICAgICBlbnZmaWxlLndyaXRlKGYnV09SS1NQQUNFRElSPXtfd29ya3NwYWNlZGlyYmF0Y2h9XG4nKQ0KICAgICAgICBlbnZmaWxlLndyaXRlKGYnVE9QTEVWRUxNT0RVTEU9e190b3BsZXZlbG1vZHVsZX1cbicpDQogICAgICAgIGVudmZpbGUud3JpdGUoZidNQUlOX1NDUklQVF9GSUxFPXtfbWFpbl9zY3JpcHRfZmlsZX1cbicpDQoNCg0KZGVmIG1vZGlmeV9hY3RpdmF0ZV9iYXQoKToNCg0KICAgIHdpdGggb3BlbihSRUxfQUNUSVZBVEVfU0NSSVBUX1BBVEgsICdyJykgYXMgb3JpZ2JhdDoNCiAgICAgICAgX2NvbnRlbnQgPSBvcmlnYmF0LnJlYWQoKQ0KICAgIGlmIFJFUExBQ0VNRU5UIG5vdCBpbiBfY29udGVudDoNCiAgICAgICAgX25ld19jb250ZW50ID0gX2NvbnRlbnQucmVwbGFjZShyJ0BlY2hvIG9mZicsIFJFUExBQ0VNRU5UKQ0KICAgICAgICB3aXRoIG9wZW4oUkVMX0FDVElWQVRFX1NDUklQVF9QQVRILCAndycpIGFzIG5ld2JhdDoNCiAgICAgICAgICAgIG5ld2JhdC53cml0ZShfbmV3X2NvbnRlbnQpDQoNCg0KaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzoNCiAgICBjcmVhdGVfcHJvamVjdF9tZXRhX2Vudl9maWxlKCkNCiAgICBtb2RpZnlfYWN0aXZhdGVfYmF0KCkNCg=='
POST_SETUP_SCRIPTS__TXT = b'Li5cLnZlbnZcU2NyaXB0c1xweXF0NXRvb2xzaW5zdGFsbHVpYy5leGUNCiVPTERIT01FX0ZPTERFUiVjcmVhdGVfdmVudl9leHRyYV9lbnZ2YXJzLnB5LCVPTERIT01FX0ZPTERFUiUgJVBST0pFQ1RfTkFNRSU='
PRE_SETUP_SCRIPTS__TXT = b'IkM6XFByb2dyYW0gRmlsZXMgKHg4NilcTWljcm9zb2Z0IFZpc3VhbCBTdHVkaW9cMjAxOVxDb21tdW5pdHlcVkNcQXV4aWxpYXJ5XEJ1aWxkXHZjdmFyc2FsbC5iYXQiLGFtZDY0DQpwc2tpbGw2NCxEcm9wYm94'
REQUIRED_DEV__TXT = b'aHR0cHM6Ly9naXRodWIuY29tL3B5aW5zdGFsbGVyL3B5aW5zdGFsbGVyL3RhcmJhbGwvZGV2ZWxvcA0KcGVwNTE3DQpudWl0a2ENCm1lbW9yeS1wcm9maWxlcg0KbWF0cGxvdGxpYg0KaW1wb3J0LXByb2ZpbGVyDQpvYmplY3RncmFwaA0KcGlwcmVxcw0KcHlkZXBzDQpudW1weT09MS4xOS4z'
REQUIRED_FROM_GITHUB__TXT = b'aHR0cHM6Ly9naXRodWIuY29tL292ZXJmbDAvQXJtYWNsYXNzLmdpdA=='
REQUIRED_MISC__TXT = b'SmluamEyDQpweXBlcmNsaXANCnJlcXVlc3RzDQpuYXRzb3J0DQpiZWF1dGlmdWxzb3VwNA0KcGRma2l0DQpjaGVja3N1bWRpcg0KY2xpY2sNCm1hcnNobWFsbG93DQpyZWdleA0KcGFyY2UNCmpzb25waWNrbGUNCmZ1enp5d3V6enkNCmZ1enp5c2VhcmNoDQpweXRob24tTGV2ZW5zaHRlaW4NCg=='
REQUIRED_PERSONAL_PACKAGES__TXT = b'RDpcRHJvcGJveFxob2JieVxNb2RkaW5nXFByb2dyYW1zXEdpdGh1YlxNeV9SZXBvc1xnaWR0b29sc191dGlscyxnaWR0b29scw0KRDpcRHJvcGJveFxob2JieVxNb2RkaW5nXFByb2dyYW1zXEdpdGh1YlxNeV9SZXBvc1xnaWRxdHV0aWxzLGdpZHF0dXRpbHMNCkQ6XERyb3Bib3hcaG9iYnlcTW9kZGluZ1xQcm9ncmFtc1xHaXRodWJcTXlfUmVwb3NcZ2lkbG9nZ2VyX3JlcCxnaWRsb2dnZXINCkQ6XERyb3Bib3hcaG9iYnlcTW9kZGluZ1xQcm9ncmFtc1xHaXRodWJcTXlfUmVwb3NcR2lkX1ZzY29kZV9XcmFwcGVyLGdpZF92c2NvZGVfd3JhcHBlcg0KRDpcRHJvcGJveFxob2JieVxNb2RkaW5nXFByb2dyYW1zXEdpdGh1YlxNeV9SZXBvc1xHaWRfVmlld19tb2RlbHMsZ2lkX3ZpZXdfbW9kZWxzDQpEOlxEcm9wYm94XGhvYmJ5XE1vZGRpbmdcUHJvZ3JhbXNcR2l0aHViXE15X1JlcG9zXEdpZGNvbmZpZyxnaWRjb25maWc='
REQUIRED_QT__TXT = b'UHlRdDUNCnB5b3BlbmdsDQpQeVF0M0QNClB5UXRDaGFydA0KUHlRdERhdGFWaXN1YWxpemF0aW9uDQpQeVF0V2ViRW5naW5lDQpRU2NpbnRpbGxhDQpweXF0Z3JhcGgNCnBhcmNlcXQNClB5UXRkb2MNCnB5cXQ1LXRvb2xzDQpQeVF0NS1zdHVicw0KcHlxdGRlcGxveQ=='
REQUIRED_TEST__TXT = b'cHl0ZXN0DQpweXRlc3QtcXQ='

root_folder_data = {'create_venv.cmd': CREATE_VENV__CMD, 'create_venv_extra_envvars.py': CREATE_VENV_EXTRA_ENVVARS__PY, }

venv_setup_settings_folder_data = {'post_setup_scripts.txt': POST_SETUP_SCRIPTS__TXT, 'pre_setup_scripts.txt': PRE_SETUP_SCRIPTS__TXT, 'required_dev.txt': REQUIRED_DEV__TXT, 'required_from_github.txt': REQUIRED_FROM_GITHUB__TXT,
                                   'required_misc.txt': REQUIRED_MISC__TXT, 'required_personal_packages.txt': REQUIRED_PERSONAL_PACKAGES__TXT, 'required_qt.txt': REQUIRED_QT__TXT, 'required_test.txt': REQUIRED_TEST__TXT, }


def pathmaker(first_segment, *in_path_segments, rev=False):
    """
    Normalizes input path or path fragments, replaces '\\\\' with '/' and combines fragments.

    Parameters
    ----------
    first_segment : str
        first path segment, if it is 'cwd' gets replaced by 'os.getcwd()'
    rev : bool, optional
        If 'True' reverts path back to Windows default, by default None

    Returns
    -------
    str
        New path from segments and normalized.
    """
    _first = os.getcwd() if first_segment == 'cwd' else first_segment
    _path = os.path.join(_first, *in_path_segments)
    _path = _path.replace('\\\\', '/')
    _path = _path.replace('\\', '/')
    if rev is True:
        _path = _path.replace('/', '\\')

    return _path.strip()


def pack_data():
    _folder = pathmaker('cwd', 'create_venv_tool')

    a = shutil.make_archive(pathmaker('cwd', 'create_venv_tool_archive'), format='zip', root_dir=_folder)
    return pathmaker(a)


def convert_to_bin(file, use_base64=False):
    with open(file, 'rb') as binf:
        _content = binf.read()
    if use_base64 is True:
        _content = base64.b64encode(_content)
    return _content


def collect_files():
    for dirname, folderlist, filelist in os.walk(r"D:\Dropbox\hobby\Modding\Programs\Github\My_Repos\Tool_Vault\misc\temp_tool_storage\create_venv_tool"):
        for _file in filelist:
            _path = pathmaker(dirname, _file)
            _name = _file.replace('.', '__').upper()
            _typus = _file.split('.')[-1]
            _bin_content = convert_to_bin(_path, True)
            yield FILE_TUPLE(_name, _path, _typus, _bin_content)


def write_the_data_file():
    _out_list = []
    _folder_dict = {'root': [], 'venv_setup_settings': []}
    for item in collect_files():
        _out_list.append(f"{item.name} = {item.bin_content}")
        if item.typus == 'txt':
            _folder_dict['venv_setup_settings'].append(item.name)
        else:
            _folder_dict['root'].append(item.name)
    with open("build_create_venv_tool_data.py", 'w') as ouf:
        ouf.write('\n'.join(_out_list) + '\n\n')
        for key, value in _folder_dict.items():
            _out_string = f"{key}_folder_data = " + "{"
            for item in value:
                _out_string += f"'{item.replace('__','.').lower()}':{item},"
            _out_string += "}\n\n"
            ouf.write(_out_string)


def is_existing_path(in_path, delete=True, typus='folder'):
    if typus == 'folder':
        if os.path.isdir(in_path) is True:
            if delete is not True:
                return True
            shutil.rmtree(in_path)
        return False

    elif typus == 'file':
        if os.path.isfile(in_path) is True:
            if delete is not True:
                return True
            os.remove(in_path)
        return False


def create_folder(in_folder, delete=True):
    if is_existing_path(in_folder, delete, 'folder') is False and in_folder != 'root':
        os.makedirs(in_folder)


def create_file(in_file, bin_data, delete=True):
    if is_existing_path(in_file, delete, 'file') is False:
        _converted_bin_data = base64.b64decode(bin_data)
        with open(in_file, 'wb') as new_file:
            new_file.write(_converted_bin_data)


def exchange_placeholder(in_file, replacement):
    with open(in_file, 'r') as fi:
        _content = fi.read()
    _content = _content.replace(PROJECT_NAME_PLACEHOLDER, replacement)
    with open(in_file, 'w') as outfi:
        outfi.write(_content)


def deploy():
    cliparser = argparse.ArgumentParser(description="deploys the new create_venv.cmd script")
    cliparser.add_argument('-pj', '--project-name', required=True, help='Name of the project, where the script will be build')
    cliparser.add_argument('-nd', '--no-delete', required=False, action='store_false', help='flag to not overwrite or delete existing files of the tool in the target dir')
    cliparser.add_argument('basepath', help='Base folder of the target Workspace')
    _args = cliparser.parse_args()
    _tool_folder = pathmaker(_args.basepath, "tools")
    create_folder(_tool_folder, False)
    for file_name, file_data in root_folder_data.items():
        _file_path = pathmaker(_tool_folder, file_name)
        create_file(_file_path, file_data, _args.no_delete)
        exchange_placeholder(_file_path, _args.project_name)
    _settings_folder = pathmaker(_tool_folder, 'venv_setup_settings')
    create_folder(_settings_folder, _args.no_delete)
    for file_name, file_data in venv_setup_settings_folder_data.items():
        _file_path = pathmaker(_settings_folder, file_name)
        create_file(_file_path, file_data, _args.no_delete)
        exchange_placeholder(_file_path, _args.project_name)
    print('done')


if __name__ == '__main__':
    deploy()
