import requests
import time

def test_proxy(proxy, url="https://httpbin.org/ip"):
    """Testa o proxy em relação ao tempo de resposta, IP e anonimato"""
    try:
        start_time = time.time()
        response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=5)
        response_time = time.time() - start_time
        data = response.json()

        if response.status_code == 200:
            ip = data.get("origin")
            anonymous = "anonymous" if "X-Forwarded-For" in response.headers else "transparent"
            return {
                "proxy": proxy,
                "response_time": response_time,
                "ip": ip,
                "anonymity": anonymous
            }
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None

def validate_proxies(proxy_list):
    """Valida a lista de proxies"""
    valid_proxies = []
    for proxy in proxy_list:
        result = test_proxy(proxy)
        if result:
            valid_proxies.append(result)
    return valid_proxies

if __name__ == "__main__":
    proxies = [
        "http://198.51.100.1:8080",
        "http://203.0.113.1:8080"
    ]
    valid_proxies = validate_proxies(proxies)
    for proxy in valid_proxies:
        print(f"Proxy: {proxy['proxy']} - Response time: {proxy['response_time']}s - IP: {proxy['ip']} - Anonymity: {proxy['anonymity']}")
