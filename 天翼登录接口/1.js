const CryptoJS = require('crypto-js')
const { NodeRSA } = require('node-rsa')
const PUBLIC_KEY = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDky91Sokyr2UI/K87VMiZp/Pmiggg4fFKgclUZoPCoO+FvdeU/wSvv59Z6fEZi4Uvtzzv5UqCMfFRykokoiGSq8B3X1kr24RbtsWif/+pxfRDCA8tXw3V2DIZ/a03tg8BBgQLpdWuwTmM1448WFIs5O9pyFgjKDFoo5cWvs88HBQIDAQAB"

get_cp = function (randomStr, publicKey) {
    var n = CryptoJS.enc.Utf8.parse(randomStr)
    n = CryptoJS.enc.Base64.stringify(n)
    var key = new NodeRSA()
    key.importKey('-----BEGIN PUBLIC KEY-----\n' + publicKey + '\n-----END PUBLIC KEY-----', 'public')
    key.setOptions({ encryptionScheme: 'pkcs1' })
    return key.encrypt(n, 'base64')
}

get_pb = function (data, randomStr) {
    var t = JSON.stringify(data)
    var n = CryptoJS.enc.Utf8.parse(randomStr)
    n = CryptoJS.enc.Base64.stringify(n)
    var i = CryptoJS.enc.Base64.parse(n)
    var encrypted = CryptoJS.AES.encrypt(t, i, {
        iv: i,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    })
    return encrypted.ciphertext.toString()
}

// 生成 16 位随机字符串
var randomStr = ''
var chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
for (var i = 0; i < 16; i++) {
    randomStr += chars[Math.floor(36 * Math.random())]
}

// 准备数据（对应 3.js 中加载验证码时的 JSON）
var data = {
    "appId": "E_189",
    "captchaType": 1,
    "referer": "https://open.e.189.cn/api/logbox/separate/web/index.html?appId=E_189&lt=01EC4DD16E9ECC61CB5D009B2F65F88B6A7DA261E021AF28C96A2A68AC17B1454CB249EF3753FBE78005DA085983DC71EDEC0828B1C5F99063BDCE255101ED6B79EA6E42AA987D22D2AE19B18D53B96C2EDC91F8&reqId=0a5007004f9e488691e2060e79962e1d&encryptUrl=8E8BD2989F169B69B202137391188971E3586DC1DB772E7ADD36D3FE26AFAFE994FF164B69847B1AC91324B456B50231B4F919370661B7CA32EA47A6B87F2A42DCAFF7B92BF783F304B7A074BCD4405E3DD6BADDD3FD661A9708F54D88E2A041FE2BB84498E350BE8129B5E11F336928B9EE4554AC53EE5F0425770E7D628BEFC379C2C3AA55278CAE3FDCDAE3DE2422026CB1FFC2211332CE497C0E27C8A85F0FEEB303",
    "time": Date.now(),
    "finger": 3881141159,
    "width": "310"
}
// 分别调用生成 cp 和 pb
var cp = get_cp(randomStr, PUBLIC_KEY)
var pb = get_pb(data, randomStr)

console.log('randomStr:', randomStr)
console.log('cp:', cp)
console.log('pb:', pb)


function get_reqId() {
    for (var n, a = "abcdefghijklmnopqrstuvwxyz0123456789", i = "", c = 0; c < 32; c++)
        n = Math["floor"](36 * Math["random"]()),
            i += a.split("")[n];
    return i
}

function l() { }
function y(t, i, r) {
    null != t && ("number" == typeof t ? this.fromNumber(t, i, r) : null == i && "string" != typeof t ? this["fromString"](t, 256) : this["fromString"](t, i))
}
function get_user(t, i) {
    for (var s = new Array, n = t["length"] - 1; 0 <= n && 0 < i;) {
        var e = t["charCodeAt"](n--);
        e < 128 ? s[--i] = e : 127 < e && e < 2048 ? (s[--i] = 63 & e | 128,
            s[--i] = e >> 6 | 192) : (s[--i] = 63 & e | 128,
                s[--i] = e >> 6 & 63 | 128,
                s[--i] = e >> 12 | 224)
    }
    s[--i] = 0;
    for (var h = new l, o = new Array; 2 < i;) {
        for (o[0] = 0; 0 == o[0];)
            h["nextBytes"](o);
        s[--i] = o[0]
    }
    return s[--i] = 2,
        s[--i] = 0,
        new y(s)
}
// get_user('13535353535', 128) // 原调用缺少 l.prototype.nextBytes 和 y 的完整实现，会报错

// ============================================================
// 以下等效于 5.js 第1331行 g.prototype.encrypt(text) 及其依赖的简化实现
// 原函数依赖 JSEncrypt 的完整 BigInteger 库 + ARC4 随机数生成器（约800+行）
// 这里使用 Node.js 内置 crypto 模块实现完全等效的 RSA/ECB/PKCS1Padding 加密
// 流程：UTF-8编码 -> PKCS#1 v1.5 填充 -> RSA模幂 -> Hex输出（奇数长度前补0）
// ============================================================

const crypto = require('crypto');

function encrypt(text, publicKeyBase64) {
    publicKeyBase64 = publicKeyBase64 || PUBLIC_KEY;
    if (!publicKeyBase64) {
        console.error('Invalid RSA public key');
        return null;
    }
    try {
        var keyPem = '-----BEGIN PUBLIC KEY-----\n' + publicKeyBase64 + '\n-----END PUBLIC KEY-----';
        // 等效于 5.js 中的 doPublic(modPowInt) + hex格式化
        var encrypted = crypto.publicEncrypt({
            key: keyPem,
            padding: crypto.constants.RSA_PKCS1_PADDING
        }, Buffer.from(text, 'utf8'));
        var hex = encrypted.toString('hex');
        // 等效于 5.js 中的 0 == (1 & hex.length) ? hex : "0" + hex
        return (hex.length % 2 === 1) ? '0' + hex : hex;
    } catch (e) {
        console.error(e);
        return null;
    }
}

console.log("encrypt('13535353535'):", encrypt('13535353535'));