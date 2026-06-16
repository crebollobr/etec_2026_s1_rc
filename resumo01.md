# Resumo do Semestre — Redes de Computadores (foco na Prova 01)

**Curso:** ETEC 2026 — 1º Semestre — RC
**Repositório:** https://github.com/crebollobr/etec_2026_s1_rc
**Para a Prova 01** (aulas 16/06 e 23/06): o foco está em **HTTPS / Criptografia / Certificados** e **Proxy Reverso**. As demais aulas dão a base e aparecem no mapa abaixo.

---

## 🗺️ Mapa do Semestre (visão geral)

| Aula | Tema | Pontos-chave |
|---|---|---|
| 24/02 | Fundamentos de redes | O que é rede; LAN / MAN / WAN; switch vs roteador |
| 03/03 | Modelo TCP/IP | 4 camadas (Aplicação, Transporte, Internet, Acesso); switch (L2/MAC) × roteador (L3/IP) |
| 03/03 | Topologias e acesso ao meio | Estrela, barramento, anel, malha; CSMA/CD, CSMA/CA, Token; simplex/half/full-duplex |
| 10/03 | Modelo OSI | 7 camadas; hub (L1), switch (L2), roteador (L3); OSI × TCP/IP |
| 17/03 | Como os dados viajam | OSI/TCP-IP; ICMP e HTTP; Cisco Packet Tracer |
| 24/03 | Roteamento e TCP | Pacotes "saltando" entre roteadores; **handshake TCP (SYN, SYN-ACK, ACK)** |
| 31/03 | Protocolos HTTP e SMTP | RFCs; **portas 80 (HTTP) e 443 (HTTPS)**; testes com telnet/openssl |
| 07/04 | Roteamento e NAT (Linux/QEMU) | IP forwarding; isolamento de rede; NAT/masquerading |
| 14/04 | Análise de tráfego (Wireshark) | Filtros; inspeção de HTTP e DNS |
| 28/04 | TCP × UDP (Wireshark) | TCP confiável × UDP rápido; QUIC/HTTP3 |
| 05/05 | Sockets e captura | **Socket = IP + porta**; handshake TCP; TCP × UDP |
| 12/05 | Proxy | **Forward proxy × reverse proxy**; Python |
| 26/05 | SSH em Docker | SSH/SFTP; chaves públicas; hardening contra força bruta |
| 02/06 | HTTPS com Nginx | TLS; criptografia assimétrica; certificado autoassinado; reverse proxy |
| 09/06 | Camada de Aplicação / HTTP | Métodos **GET, POST, PUT, DELETE**; idempotência; servidor de arquivos × de aplicação |
| **16/06** | **HTTPS e Certificados** ⭐ | **Criptografia, chaves, certificado digital, CA, cadeia de confiança, OpenSSL** |
| **23/06** | **Proxy Reverso** ⭐ | **Forward × reverse, terminação TLS, Nginx, balanceamento, X-Forwarded-For** |
| 30/06 | WAF (firewall de aplicação) | Camada 7; SQL Injection, XSS, Path Traversal; rate limiting; HTTP 403 |

⭐ = conteúdo central da Prova 01.

---

## ⭐ FOCO DA PROVA 01

### 1) Criptografia

- **Simétrica:** uma **única chave** cifra e decifra. É rápida, mas exige trocar a chave com segurança.
- **Assimétrica:** usa um **par de chaves** ligadas — **pública** e **privada**.
  - A **chave pública** pode ser distribuída livremente; ela **cifra** ("tranca") os dados.
  - A **chave privada** é **secreta**; só ela **decifra** ("destranca") o que a pública trancou.
  - Resolve o problema da troca de chave da criptografia simétrica.

### 2) Certificado digital e Autoridade Certificadora (CA)

- **Certificado digital:** documento que contém a **identidade (CN)**, a **chave pública**, o **período de validade** e a **assinatura da CA**.
- **CA (Autoridade Certificadora):** entidade **confiável** que verifica e **assina** certificados. O navegador já confia em CAs Raiz conhecidas.
- **Cadeia de confiança:** **CA Raiz → CA Intermediária → Certificado do Servidor** (cada nível assina o próximo).
- **Certificado autoassinado (self-signed):** o **dono (subject)** e o **emissor (issuer)** são o mesmo — não há confiança externa (usado só em teste/desenvolvimento).
- **3 perguntas que o navegador faz ao validar um certificado:**
  1. A cadeia chega a uma **CA confiável**?
  2. O certificado está **dentro da validade**?
  3. O **domínio acessado** corresponde ao **CN** do certificado?

### 3) HTTPS / TLS

- HTTPS = HTTP + **TLS** (criptografia). Roda na **porta 443** (o HTTP puro fica na **porta 80**).
- O TLS usa criptografia **assimétrica** para estabelecer a conexão de forma segura.
- **OpenSSL:** ferramenta de linha de comando usada para **gerar chaves e certificados** (`openssl genrsa`, `openssl req -x509`, `openssl s_client`, etc.).

### 4) Proxy Reverso

- **Proxy** = intermediário ("procurador") que age em nome de alguém.
- **Forward proxy:** fica do lado do **cliente** (ex.: filtra/registra a navegação dos funcionários).
- **Proxy reverso:** fica do lado do **servidor** — é o **ponto único de entrada**; o visitante fala com o "porteiro", que repassa ao servidor real (escondido em rede interna).
- **Benefícios do proxy reverso:**
  - 🔒 **Terminação TLS** — cuida do HTTPS/certificados **em um único lugar**.
  - 🙈 **Esconde o backend** — os servidores reais ficam invisíveis em rede interna.
  - 🪢 **Balanceamento de carga** — distribui as requisições entre vários servidores.
  - 🚪 **Roteamento e controle central** — log, bloqueio e limite de requisições.
- **Nginx:** servidor mais usado em produção como proxy reverso.
- **Cabeçalho `X-Forwarded-For`:** como o backend recebe a conexão **do proxy** (ex.: 127.0.0.1), esse cabeçalho **preserva o IP original do cliente** — essencial para logs e regras de firewall.

---

## ✅ Checklist rápido para a Prova 01

- [ ] Sei diferenciar criptografia **simétrica** (1 chave) de **assimétrica** (par de chaves).
- [ ] Sei o que cada chave faz: **pública cifra**, **privada decifra** (e é secreta).
- [ ] Sei o que um **certificado** contém e o que faz uma **CA**.
- [ ] Entendo a **cadeia de confiança** e o que é um certificado **autoassinado**.
- [ ] Sei que **HTTPS = porta 443** e que o **OpenSSL** gera chaves/certificados.
- [ ] Sei diferenciar **forward** de **reverse proxy**.
- [ ] Conheço os **benefícios** do proxy reverso (terminação TLS, esconder backend, balanceamento).
- [ ] Sei para que serve o **`X-Forwarded-For`** e que o **Nginx** é o proxy reverso mais usado.
