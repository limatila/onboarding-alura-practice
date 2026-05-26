# Sobre Regex

## Padrões usados

### Caracteres literais

Verifica se a string contém exatamente o caractere especificado.

- `a` corresponde a letra "a"
- `1` corresponde ao número "1"
- `@` corresponde ao símbolo "@"

### Caracteres especiais

Verifica padrões específicos, tratando caracteres de forma agrupada e semelhante a cada regra

- `.` corresponde a qualquer caractere (exceto nova linha)
- `\d` corresponde a qualquer dígito (0-9)
- `\w` corresponde a qualquer caractere alfanumérico (letras e dígitos)
- `\s` corresponde a qualquer caractere de espaço em branco (espaço, tabulação, etc.)
- `\b` corresponde a uma borda de palavra (início ou fim de uma palavra)
- `^` corresponde ao início da string
- `$` corresponde ao final da string
- `|` corresponde a uma alternativa (ou)

### Quantificadores

Verifica a quantidade de vezes que um elemento deve ocorrer para corresponder ao padrão.

- `*` corresponde a zero ou mais ocorrências do elemento anterior
- `+` corresponde a uma ou mais ocorrências do elemento anterior
- `?` corresponde a zero ou uma ocorrência do elemento anterior

- `{n,m}` estabelece um range a entre **n** e **m** ocorrências do elemento anterior\

## Modo de construção de um Regex

1. Definir o padrão que deseja encontrar
2. Identificar os caracteres literais e especiais necessários para o padrão <br>
2.1 Utilizar quantificadores para especificar a quantidade de ocorrências

A concatenação dos padrões do Regex montado corresponde a ordem com a que esses padrões devem aparecer na string para que haja uma correspondência bem-sucedida.

### Exemplos

- telefone brasileiro: `^\(\d{2}\)\s\d{4,5}-\d{4}$` normaliza qualquer numero `(XX) XXXX-XXXX` ou `(XX) XXXXX-XXXX`
- email: `^[\w.-]+@[\w.-]+\.\w{2,4}$` normaliza qualquer combinacao padrão como `test@testmail.com.br`
- data: `^\d{2}/\d{2}/\d{4}$` normaliza qualquer data no formato `DD/MM/AAAA`
