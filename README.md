# DL Project

Оригинальный проект : https://github.com/sicara/tf-explain


## Инструкция по сборке

1. Склонируйте репозиторий
```
git clone https://github.com/MADZEROPIE/DL.git
```
2. Перейдите в склонированную папку "DL"
```
cd DL
```
3. Далее необходимо собрать докер
```
docker build . --tag explainer
```
4. Запускаем докер explainer со свойством монтирования в папку DL/images/result
```
docker run -v $(pwd)/images/result:/src explainer
```
5. Чтобы снести всё в системе (КРАЙНЕ РАДИКАЛЬНЫЙ СПОСОБ!)
```
docker rm -vf $(docker ps -aq)
docker rmi -f $(docker images -aq)
```
