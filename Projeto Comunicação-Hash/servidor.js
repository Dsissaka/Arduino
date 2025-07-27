const fs = require('fs');
const http = require('http');
const WebSocket = require('ws');

// O nome do arquivo que o script Python está gerando
const jsonFilePath = './dados.json'; 

// Servidor HTTP simples para servir o seu painel (dashboard)
const server = http.createServer((req, res) => {
  fs.readFile('./index.html', (err, data) => { // Assume que você tem um index.html
    if (err) {
      res.writeHead(500);
      return res.end('Erro ao carregar o painel de visualização (index.html)');
    }
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
    res.end(data);
  });
});

const wss = new WebSocket.Server({ server });

const broadcastData = () => {
  fs.readFile(jsonFilePath, 'utf8', (err, fileContent) => {
    if (err) {
      // Se o arquivo ainda não existe, não faz nada.
      if (err.code === 'ENOENT') {
        console.log("Aguardando a criação do arquivo de dados...");
        return;
      }
      console.error("Erro ao ler o arquivo JSON:", err);
      return;
    }

    // Apenas verifica se o conteúdo não está vazio antes de enviar
    if (fileContent.trim() === '') {
        console.log("Arquivo de dados está vazio, nada a enviar.");
        return;
    }
    
    // Tenta validar se o conteúdo é um JSON válido antes de enviar.
    // Isso previne enviar um arquivo que foi salvo pela metade.
    try {
        JSON.parse(fileContent); // Se isso não gerar erro, o JSON é válido.
        console.log(`Arquivo válido. Enviando dados para ${wss.clients.size} clientes.`);
        
        // Envia o conteúdo completo do arquivo para todos os clientes.
        wss.clients.forEach(client => {
          if (client.readyState === WebSocket.OPEN) {
            client.send(fileContent);
          }
        });
    } catch (parseError) {
        console.warn("Arquivo JSON corrompido ou incompleto, ignorando envio.", parseError.message);
    }
  });
};

wss.on('connection', ws => {
  console.log('Cliente conectado ao WebSocket.');
  broadcastData(); // Envia os dados atuais assim que um cliente se conecta
  ws.on('close', () => console.log('Cliente desconectado.'));
});

// Monitora o arquivo por mudanças.
fs.watch(jsonFilePath, (eventType) => {
  if (eventType === 'change') {
    console.log('Arquivo dados.json modificado. Enviando atualização...');
    broadcastData();
  }
});

const port = 8080;
server.listen(port, () => {
  console.log(`Servidor rodando. Abra http://localhost:${port} no seu navegador.`);
});
