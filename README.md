# ⚙️ TOASTER.SESSION-CHECKER-SERVICE

![main_img](https://github.com/STALCRAFT-FUNCKA/toaster.message-handling-service/assets/76991612/8bb6b3bf-8385-4d4b-80cc-e104d5283a9c)

## 📄 Информация
**TOASTER.SESSION-CHECKER-SERVICE** - сервис, выполняющий роль "уборщика мусора".

В процессе работы TOASTER будут создаваться кнопочные меню, которые по-хорошему необходимо удалять через некоторое время.

Сервис раз в 1 минуту проверяет таблицу БД с информацией о текущихз сессиях и пытается найти те, которые уже должны быть просрочены. После чего он благополучно удаляет сообщения с сессиями меню.

### Дополнительно
Docker stup:
```
docker network
    name: TOASTER
    ip_gateway: 172.18.0.1
    subnet: 172.18.0.0/16
    driver: bridge


docker image
    name: toaster.session-checker-service
    args:
        TOKEN: "..."
        GROUPID: "..."
        SQL_HOST: "..."
        SQL_PORT: "..."
        SQL_USER: "..."
        SQL_PSWD: "..."


docker container
    name: toaster.session-checker-service
    network_ip: 172.1.08.10

docker volumes:
    /var/log/TOASTER/toaster.session-checker-service:/service/logs
```

Jenkins shell command:
```
imageName="toaster.session-checker-service"
containerName="toaster.session-checker-service"
localIP="172.18.0.10"
networkName="TOASTER"

#stop and remove old container
docker stop $containerName || true && docker rm -f $containerName || true

#remove old image
docker image rm $imageName || true

#build new image
docker build . -t $imageName \
--build-arg TOKEN=$TOKEN \
--build-arg GROUPID=$GROUPID \
--build-arg SQL_HOST=$SQL_HOST \
--build-arg SQL_PORT=$SQL_PORT \
--build-arg SQL_USER=$SQL_USER \
--build-arg SQL_PSWD=$SQL_PSWD

#run container
docker run -d \
--name $containerName \
--volume /var/log/TOASTER/$imageName:/service/logs \
--restart always \
$imageName

#network setup
docker network connect --ip $localIP $networkName $containerName

#clear chaches
docker system prune -f
```
