# Resumo Geral do Semestre — Redes de Computadores

**Curso:** ETEC 2026 — 1º Semestre — RC
**Repositório:** https://github.com/crebollobr/etec_2026_s1_rc
**Material de estudo para a Prova 01 (23/06) e a Prova 02 / recuperação (30/06)** — ambas cobrem **todo o semestre**.

---

## 🗺️ Mapa do Semestre

| Aula | Tema | Pontos-chave |
|---|---|---|
| 24/02 | Fundamentos de redes | O que é rede; LAN / MAN / WAN; switch vs roteador |
| 03/03 | Modelo TCP/IP | 4 camadas (Aplicação, Transporte, Internet, Acesso); switch (L2/MAC) × roteador (L3/IP) |
| 03/03 | Topologias e acesso ao meio | Estrela, barramento, anel, malha; CSMA/CD, CSMA/CA, Token; simplex/half/full-duplex |
| 10/03 | Modelo OSI | 7 camadas; hub (L1), switch (L2), roteador (L3); OSI × TCP/IP |
| 17/03 | Como os dados viajam | OSI/TCP-IP; ICMP e HTTP; Cisco Packet Tracer |
| 24/03 | Roteamento e TCP | Pacotes "saltando" entre roteadores; handshake TCP (SYN, SYN-ACK, ACK) |
| 31/03 | Protocolos HTTP e SMTP | RFCs; portas 80 (HTTP) e 443 (HTTPS); testes com telnet/openssl |
| 07/04 | Roteamento e NAT (Linux/QEMU) | IP forwarding; isolamento de rede; NAT/masquerading |
| 14/04 | Análise de tráfego (Wireshark) | Filtros; inspeção de HTTP e DNS |
| 28/04 | TCP × UDP (Wireshark) | TCP confiável × UDP rápido; QUIC/HTTP3 |
| 05/05 | Sockets e captura | Socket = IP + porta; handshake TCP; TCP × UDP |
| 12/05 | Proxy | Forward proxy × reverse proxy; Python |
| 26/05 | SSH em Docker | SSH/SFTP; chaves públicas; hardening contra força bruta |
| 02/06 | HTTPS com Nginx | TLS; criptografia assimétrica; certificado autoassinado; reverse proxy |
| 09/06 | Camada de Aplicação / HTTP | Métodos GET, POST, PUT, DELETE; idempotência; servidor de arquivos × de aplicação |
| 16/06 | HTTPS e Certificados | Criptografia, chaves, certificado digital, CA, cadeia de confiança, OpenSSL |
| 23/06 | Proxy Reverso | Forward × reverse, terminação TLS, Nginx, balanceamento, X-Forwarded-For |
| 30/06 | WAF (firewall de aplicação) | Camada 7; SQL Injection, XSS, Path Traversal; rate limiting; HTTP 403 |

---

## 1) Fundamentos de Redes

- **Rede de computadores:** conjunto de dispositivos conectados que trocam informações.
- **Classificação por alcance:** **LAN** (local — sala/prédio), **MAN** (cidade), **WAN** (longas distâncias / mundial).
- **Equipamentos:**
  - **Hub** (camada 1) — repete o sinal para todos (antigo).
  - **Switch** (camada 2) — comunicação **interna** da rede, usa endereço **MAC**.
  - **Roteador** (camada 3) — **conecta redes diferentes**, usa endereço **IP**.
- **Topologias:** estrela (mais resiliente), barramento, anel, malha.
- **Modos de transmissão:** simplex (1 sentido), half-duplex (reveza), full-duplex (os dois ao mesmo tempo).

## 2) Modelos de Camadas

- **OSI:** 7 camadas (modelo teórico de referência).
- **TCP/IP:** 4 camadas — **Aplicação, Transporte, Internet, Acesso à Rede** (modelo prático da internet).
- **Dispositivos por camada:** hub = L1, switch = L2 (MAC), roteador = L3 (IP).

## 3) Camada de Transporte (TCP × UDP)

- **TCP:** confiável e **orientado a conexão** (garante a entrega e a ordem).
- **UDP:** rápido e **sem conexão** ("fire-and-forget"), sem garantia de entrega.
- **Handshake TCP (3 vias):** **SYN → SYN-ACK → ACK** (estabelece a conexão antes de enviar dados).
- **Socket:** combinação de **endereço IP + porta**.
- **QUIC / HTTP3:** roda sobre UDP, recuperando a confiabilidade do TCP com mais velocidade.

## 4) Camada de Internet / Roteamento

- **Roteamento:** os pacotes "saltam" (hops) de roteador em roteador até o destino.
- **ICMP:** protocolo usado pelo **ping** (testar conectividade) e pelo traceroute.
- **NAT (masquerading):** traduz IPs **privados internos** para um **IP público**, permitindo acesso à internet.
- **IP forwarding:** faz uma máquina Linux atuar como **roteador** (encaminhar pacotes entre redes).

## 5) Camada de Aplicação

- **HTTP:** protocolo da web; **stateless** (sem estado), modelo requisição-resposta. Porta **80**.
- **HTTPS:** HTTP + TLS (criptografado). Porta **443**.
- **Métodos HTTP:** **GET** (ler — seguro), **POST** (criar/enviar — **não idempotente**), **PUT** (atualizar), **DELETE** (apagar).
- **DNS:** traduz **nomes de domínio** (sites) em **endereços IP**.
- **SMTP:** protocolo de envio de e-mail; **RFC** = documento técnico que padroniza os protocolos (IETF).

## 6) Análise de Tráfego

- **Wireshark:** ferramenta para **capturar e analisar** o tráfego da rede (filtrar por HTTP, DNS, TCP, etc.).

## 7) Segurança

- **Criptografia simétrica:** **uma única chave** cifra e decifra (rápida, mas exige troca segura da chave).
- **Criptografia assimétrica:** **par de chaves** — a **pública cifra**, a **privada** (secreta) **decifra**.
- **Certificado digital:** contém identidade (**CN**), chave pública, validade e a **assinatura da CA**.
- **CA (Autoridade Certificadora):** entidade confiável que assina certificados. **Cadeia de confiança:** Raiz → Intermediária → Servidor.
- **Certificado autoassinado:** dono e emissor iguais (sem confiança externa; só para teste).
- **OpenSSL:** ferramenta para gerar chaves e certificados.
- **Proxy reverso:** fica na frente **dos servidores** (ponto único de entrada). Benefícios: **terminação TLS**, esconder o backend, **balanceamento de carga**. O mais usado é o **Nginx**.
- **`X-Forwarded-For`:** cabeçalho que **preserva o IP original do cliente** quando a requisição passa pelo proxy.
- **SSH/SFTP:** acesso remoto **criptografado** (substitui o FTP); suporta autenticação por **chaves públicas**.
- **WAF (Web Application Firewall):** firewall na **camada de aplicação (7)** que bloqueia ataques como **SQL Injection**, **XSS** e **Path Traversal**; usa **rate limiting** e responde **HTTP 403** (proibido) ao bloquear.

---

## ✅ Checklist de estudo

- [ ] LAN/MAN/WAN e a função de hub, switch e roteador (e em que camada cada um atua).
- [ ] OSI (7 camadas) × TCP/IP (4 camadas).
- [ ] TCP × UDP e o handshake **SYN → SYN-ACK → ACK**.
- [ ] Socket = **IP + porta**; portas **80 (HTTP)** e **443 (HTTPS)**.
- [ ] Métodos HTTP (GET, POST, PUT, DELETE) e o que faz o **DNS**.
- [ ] NAT, IP forwarding e o protocolo do **ping (ICMP)**.
- [ ] Para que serve o **Wireshark**.
- [ ] Criptografia **simétrica × assimétrica**; o que é **certificado** e **CA**.
- [ ] **Forward × reverse proxy**, **Nginx**, **X-Forwarded-For**.
- [ ] **SSH** (acesso remoto seguro) e **WAF** (SQL Injection, XSS, HTTP 403).
