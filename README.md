# myssh

**If you want to read how to use in English, see README-en.md.**

## 概要

複数のサーバーを管理していると、接続するサーバーごとに打つsshコマンドを変えなくてはいけない場合があり、面倒です。
mysshコマンドを使用すると、予め決めておいた名前を入力するだけで設定が読まれ、簡単にsshできます。

## バージョン

Ver 1.0

## 使い方

### 初期設定

#### このリポジトリをダウンロードする

ダウンロード先のpathを以後 ```[dir-path]``` と記述します。

#### hosts.jsonにホストを登録する

このリポジトリのhosts.jsonはサンプルデータが含まれています。
初回使用時に、必要なホスト情報を追加してください。  
ホスト情報に記述可能なプロパティは以下の通りです:

* address **(必須)**  
接続したいホストのアドレスを指定します。通常のssh同様、IPアドレスまたはドメインを指定してください。

* port (任意)  
接続したいホストのsshポートを指定します。省略した場合は22番ポートが指定されます。

* username (任意)  
sshに使用するユーザー名を指定します。省略した場合はコマンドを実行するユーザーが指定されます。

* cert-path (任意)  
公開鍵認証を必要とする場合、使用する秘密鍵のパスを指定してください。

以上のホスト情報を、任意の名前でssh-hostsに追加してください。

#### コマンドのエイリアスを設定する

~/.bashrc に以下の記述を追加します:
```bash
alias myssh='python [dir-path]/myssh.py $1'
```
完了したら、以下を実行してください:
```bash
source ~/.bashrc
```

### 使用

```bash
myssh [hosts.jsonに指定したホスト名]
```

## 連絡先

* Twitter: [@hideo54](https://twitter.com/hideo54)
* Email: hideo54.pub@gmail.com
