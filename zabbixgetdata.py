from pyzabbix.api import ZabbixAPI

# variable imports
import cred
import variablegen


zapi = ZabbixAPI(url=cred.zab_url, user=cred.user_name, password=cred.password_zab)

test: object = zapi.do_request(method='trend.get', params={
        "output": [
                "itemid",
                "value_max"
        ],
        "itemids": [
                "23316"
        ],
        "limit": "1",
        "time_from": variablegen.unix_yesterday,
        "time_till": variablegen.unix_today,
})



print(test)
