# Proxy Tester Elite

🎯 **Objetivo**: Validar uma lista de proxies automaticamente, verificando seu tempo de resposta, IP e nível de anonimato.

## 🚀 Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/proxy-tester-elite.git
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Adicione sua lista de proxies no arquivo `proxy_tester.py`, na variável `proxies`, como uma lista de strings. 

4. Execute o script:
   ```bash
   python proxy_tester.py
   ```

## 🛠️ Funcionalidades

- **Tempo de Resposta**: Mede quanto tempo o proxy leva para responder à requisição.
- **IP do Proxy**: Verifica o IP que o proxy está utilizando.
- **Anonimato**: Determina se o proxy é anônimo ou transparente.

## 📑 Exemplo de Saída

```bash
Proxy: http://198.51.100.1:8080 - Response time: 0.5s - IP: 198.51.100.1 - Anonymity: anonymous
```

## 🔧 Dependências

- `requests`: Biblioteca para realizar requisições HTTP.
- `time`: Biblioteca para medir o tempo de resposta.

## 💡 Contribua!

Se você deseja contribuir para este projeto, sinta-se à vontade para enviar um pull request. Vamos melhorar juntos! 
