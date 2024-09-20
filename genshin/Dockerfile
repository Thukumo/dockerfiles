FROM debian:stable-slim
WORKDIR /
RUN apt update -y && apt install openjdk-17-jdk gnupg curl npm -y
RUN git clone https://github.com/Kei-Luna/LunaGC_5.0.0 && cd LunaGC_5.0.0 \
&& bash gradlew && git clone https://github.com/Kei-Luna/LunaGC_Resources_5.0.0 resources \
&& echo "org.gradle.vfs.watch=true" >> gradle.properties && bash gradlew wrapper && bash gradlew jar
WORKDIR /LunaGC_5.0.0
RUN curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor \
&& echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] http://repo.mongodb.org/apt/debian bookworm/mongodb-org/7.0 main" \
| tee /etc/apt/sources.list.d/mongodb-org-7.0.list \
&& apt update -y && apt install mongodb-org -y
VOLUME /db
COPY <<EOF /etc/mongod.conf
storage:
  dbPath: /db
net:
  bindIp: 127.0.0.1 
  port: 27017
EOF
COPY <<EOF start.sh
mongod --config /etc/mongod.conf --fork --logpath /var/log/mongodb.log
java -jar /LunaGC_5.0.0/LunaGC-5.0.0.jar
EOF
RUN cat <<EOF > config.json
{
  "folderStructure": {
    "resources": "./resources/",
    "data": "./data/",
    "packets": "./packets/",
    "scripts": "resources:Scripts/",
    "plugins": "./plugins/",
    "cache": "./cache/"
  },
  "databaseInfo": {
    "server": {
      "connectionUri": "mongodb://localhost:27017",
      "collection": "grasscutter"
    },
    "game": {
      "connectionUri": "mongodb://localhost:27017",
      "collection": "grasscutter"
    }
  },
  "language": {
    "language": "en_US",
    "fallback": "en_US",
    "document": "EN"
  },
  "account": {
    "autoCreate": true,
    "EXPERIMENTAL_RealPassword": false,
    "defaultPermissions": [
      "*"
    ],
    "maxPlayer": -1
  },
  "server": {
    "debugWhitelist": [],
    "debugBlacklist": [],
    "runMode": "HYBRID",
    "logCommands": false,
    "fastRequire": true,
    "http": {
      "startImmediately": false,
      "bindAddress": "0.0.0.0",
      "bindPort": 443,
      "accessAddress": "127.0.0.1",
      "accessPort": 0,
      "encryption": {
        "useEncryption": false,
        "useInRouting": false,
        "keystore": "./keystore.p12",
        "keystorePassword": "123456"
      },
      "policies": {
        "cors": {
          "enabled": true,
          "allowedOrigins": [
            "*"
          ]
        }
      },
      "files": {
        "indexFile": "./index.html",
        "errorFile": "./404.html"
      }
    },
    "game": {
      "bindAddress": "0.0.0.0",
      "bindPort": 22102,
      "accessAddress": "127.0.0.1",
      "accessPort": 0,
      "useUniquePacketKey": true,
      "loadEntitiesForPlayerRange": 300,
      "enableScriptInBigWorld": true,
      "enableConsole": true,
      "kcpInterval": 20,
      "logPackets": "NONE",
      "isShowPacketPayload": false,
      "isShowLoopPackets": false,
      "cacheSceneEntitiesEveryRun": false,
      "gameOptions": {
        "inventoryLimits": {
          "weapons": 5000,
          "relics": 5000,
          "materials": 5000,
          "furniture": 5000,
          "all": 30000
        },
        "avatarLimits": {
          "singlePlayerTeam": 4,
          "multiplayerTeam": 4
        },
        "sceneEntityLimit": 10000,
        "watchGachaConfig": true,
        "enableShopItems": true,
        "staminaUsage": true,
        "energyUsage": true,
        "fishhookTeleport": true,
        "trialCostumes": false,
        "forceLegacyDrops": true,
        "questing": {
          "enabled": false
        },
        "resinOptions": {
          "resinUsage": false,
          "cap": 160,
          "rechargeTime": 480
        },
        "rates": {
          "adventureExp": 1.0,
          "mora": 1.0,
          "leyLines": 1.0
        },
        "handbook": {
          "enable": false,
          "allowCommands": true,
          "limits": {
            "enabled": false,
            "interval": 3,
            "maxRequests": 10,
            "maxEntities": 25
          },
          "server": {
            "enforced": false,
            "address": "127.0.0.1",
            "port": 443,
            "canChange": true
          }
        }
      },
      "joinOptions": {
        "welcomeEmotes": [
          5001,
          5002,
          5003
        ],
        "welcomeMessage": "Welcome to a Grasscutter server! \n\nLeagcy drops are enabled by default! This lets spawned mobs have proper drops without any resource edits. \n If you want to return to the new drop system, use <color=#567d46>/s legacy</color> \n\n If you want everything unlocked, use <color=#567d46>/unlockall</color> and <color=#567d46>/give all lv90 c6 r5 sl10</color>",
        "welcomeMail": {
          "title": "Welcome to Grasscutter!",
          "content": "Hi there!\r\nFirst of all, welcome to Grasscutter. If you have any issues, please let us know so that Lawnmower can help you! \r\n\r\nCheck out our:\r\n<type=\"browser\" text=\"Discord\" href=\"https://discord.gg/T5vZU6UyeG\"/>\n",
          "sender": "Lawnmower",
          "items": [
            {
              "itemId": 13509,
              "itemCount": 1,
              "itemLevel": 1
            },
            {
              "itemId": 201,
              "itemCount": 99999,
              "itemLevel": 1
            }
          ]
        }
      },
      "serverAccount": {
        "avatarId": 10000014,
        "nameCardId": 210009,
        "adventureRank": 69,
        "worldLevel": 99,
        "nickName": "<color=#00CBFE>Kanata</color>",
        "signature": "<color=#567d46>Seek grass (talk to me!)</color>"
      },
      "visionOptions": [
        {
          "name": "VISION_LEVEL_NORMAL",
          "visionRange": 80,
          "gridWidth": 20
        },
        {
          "name": "VISION_LEVEL_LITTLE_REMOTE",
          "visionRange": 16,
          "gridWidth": 40
        },
        {
          "name": "VISION_LEVEL_REMOTE",
          "visionRange": 1000,
          "gridWidth": 250
        },
        {
          "name": "VISION_LEVEL_SUPER",
          "visionRange": 4000,
          "gridWidth": 1000
        },
        {
          "name": "VISION_LEVEL_NEARBY",
          "visionRange": 40,
          "gridWidth": 20
        },
        {
          "name": "VISION_LEVEL_SUPER_NEARBY",
          "visionRange": 20,
          "gridWidth": 20
        }
      ]
    },
    "dispatch": {
      "regions": [],
      "dispatchUrl": "ws://127.0.0.1:1111",
      "encryptionKey": "aCUylg3uLqGN6fviB4IuN2YnZB26sBTO+mlmuIZwQGo=",
      "dispatchKey": "Nr1NECFo6gDt5o23Sr1jHhfu3QcCCRY21ctBS3BbWLc=",
      "defaultName": "Grasscutter",
      "logRequests": "NONE"
    },
    "debugMode": {
      "serverLoggerLevel": {
        "levelInt": 10000,
        "levelStr": "DEBUG"
      },
      "servicesLoggersLevel": {
        "levelInt": 20000,
        "levelStr": "INFO"
      },
      "logPackets": "ALL",
      "isShowPacketPayload": false,
      "isShowLoopPackets": false,
      "logRequests": "ALL"
    }
  },
  "version": 14
}
EOF
EXPOSE 443
EXPOSE 22102/udp
CMD ["bash", "/LunaGC_5.0.0/start.sh"]
