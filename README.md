# kompasiana API

unffocial API of kompasiana.com

![GitHub contributors](https://img.shields.io/github/contributors/fiandev/flask-template)
![GitHub License](https://img.shields.io/github/license/fiandev/flask-template)
![PyPI - Version](https://img.shields.io/pypi/v/Flask)


---

## get profile info
```bash
/api/profile/<username>
```

### example
```bash
/api/profile/alfiansa
```

```javascript
{
  "code": 200,
  "data": {
    "data": {
      "avatar": "https://assets-a1.kompasiana.com/images/avatar/fiandev-66639342ed64157138305fb2.jpg?t=t&v=40&x=40",
      "level": "Debutan",
      "name": "Aditia Akbar Putra Alfiansa",
      "point": 209,
      "posts": [
        {
          "prefix": "bagaimana-cara-menarik-token-crypto-dari-airdrop-yang-telah-dikerjakan",
          "slug": "66754be7c925c40b8172d732",
          "thumbnail": "https://assets-a1.kompasiana.com/items/album/2024/06/21/9eddb919-9794-42bc-b9be-2712f360871e-66755015ed6415132c490ea2.jpeg?t=o&v=410",
          "title": "Bagaimana Cara Menarik Token Crypto dari Airdrop yang Telah Dikerjakan"
        },
        ...
      ]
    },
    "message": "success"
  },
  "status": "success"
}
```
## get user post
```bash
/api/profile/<username>/<prefix>/slug
```
```bash
/api/profile/alfiansa/66754be7c925c40b8172d732/bagaimana-cara-menarik-token-crypto-dari-airdrop-yang-telah-dikerjakan
```
```javascript
{
  "code": 200,
  "data": {
    "data": {
      "content": "<div class=\"read-content read__keyword col-lg-9 col-md-9 col-sm-9 col-xs-9\"itemprop=articleBody><p><span class=\"fr-img-caption fr-fic fr-dib\"style=width:295px><span class=fr-img-wrap></span></span><p>banyak para airdrop hunter pemula yang bertanya bagaimana cara melakukan penarikan uang dari airdrop yang kita kerjakan,<p><strong>sejatinya bukan uang secara langsung yang akan kita dapat</strong> tapi memang bisa apabila pihak penyelenggara airdrop memang mengadakan acara seperti yang paling banyak mengundang orang maka ia akan mendapat hadiah uang dan jumlah nya cukup menggiurkan, yah itu memang ada karna untuk menang memang tidaklah...",
      "images": [
        "https://assets.kompasiana.com/items/album/2024/06/21/9eddb919-9794-42bc-b9be-2712f360871e-66755015ed6415132c490ea2.jpeg?t=o&v=260",
        "https://assets-a1.kompasiana.com//statics/2019_kompasiana/images/gambar-default-karusel2.jpg?t=o&v=260"
      ],
      "tag": "Cryptocurrency",
      "thumbnail": "https://assets.kompasiana.com/items/album/2024/06/21/9eddb919-9794-42bc-b9be-2712f360871e-66755015ed6415132c490ea2.jpeg?t=o&v=770",
      "title": "Bagaimana Cara Menarik Token Crypto dari Airdrop yang Telah Dikerjakan"
    }
  },
  "status": "success"
}
```

> built with ❤️ by fiandev