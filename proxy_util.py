import zipfile

def create_proxy_extension(ip, port, username, password, ext_path):
    """Tạo extension Chrome gắn proxy auth (user:pass@ip:port)"""
    manifest_json = f"""
    {{
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "ProxyAuth",
        "permissions": ["proxy", "tabs", "unlimitedStorage", "storage", "<all_urls>", "webRequest", "webRequestBlocking"],
        "background": {{
            "scripts": ["background.js"]
        }}
    }}
    """

    background_js = f"""
    chrome.proxy.settings.set({{
        value: {{
            mode: "fixed_servers",
            rules: {{
                singleProxy: {{
                    scheme: "http",
                    host: "{ip}",
                    port: parseInt({port})
                }},
                bypassList: ["localhost"]
            }}
        }},
        scope: "regular"
    }}, function() {{}});

    chrome.webRequest.onAuthRequired.addListener(
        function(details) {{
            return {{
                authCredentials: {{
                    username: "{username}",
                    password: "{password}"
                }}
            }};
        }},
        {{urls: ["<all_urls>"]}},
        ['blocking']
    );
    """

    with zipfile.ZipFile(ext_path, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
