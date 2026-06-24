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
var randomStr = get_randomstr()
function get_randomstr() {
  r = ''
  var chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
  for (var i = 0; i < 16; i++) {
    r += chars[Math.floor(36 * Math.random())]
  }
  return r
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

//console.log('randomStr:', randomStr)
//console.log('cp:', cp)
//console.log('pb:', pb)


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




/**
 * 生成高拟真滑块拖动轨迹
 * @param {number} targetX - 目标X方向总位移（像素，正数）
 * @param {Object} [options] - 可选配置
 * @param {number} [options.minPoints=44] - 最小组数（含起始点）
 * @param {number} [options.maxPoints=85] - 最大组数（含起始点）
 * @param {number} [options.minTime=2000] - 最短滑动时间（毫秒）
 * @param {number} [options.maxTime=3000] - 最长滑动时间（毫秒）
 * @param {number} [options.randomRange=0.05] - 单步时间随机波动幅度
 * @returns {{ track: Array<{pointDiff: number, timeDiff: number}>, totalTime: number }}
 */
function generateSlideTrack(targetX, options = {}) {
  const {
    minPoints = 35,
    maxPoints = 50,
    minTime = 2000,
    maxTime = 3000,
    randomRange = 0.05
  } = options;

  // ========== 1. 固定特征阶段（保证运动形态真实，点数固定） ==========
  // 加速段：启动到峰值速度
  const phaseAccel = [
    { pointDiff: 2, timeDiff: 103 },
    { pointDiff: 3, timeDiff: 6 },
    { pointDiff: 3, timeDiff: 8 },
    { pointDiff: 5, timeDiff: 8 },
    { pointDiff: 5, timeDiff: 8 },
    { pointDiff: 6, timeDiff: 9 },
    { pointDiff: 6, timeDiff: 7 },
    { pointDiff: 7, timeDiff: 8 },
    { pointDiff: 7, timeDiff: 8 },
    { pointDiff: 6, timeDiff: 8 },
    { pointDiff: 8, timeDiff: 8 },
    { pointDiff: 8, timeDiff: 8 },
    { pointDiff: 9, timeDiff: 7 }
  ];
  // 减速段：峰值到进入微调
  const phaseDecel = [
    { pointDiff: 5, timeDiff: 8 },
    { pointDiff: 4, timeDiff: 8 },
    { pointDiff: 3, timeDiff: 8 },
    { pointDiff: 3, timeDiff: 10 },
    { pointDiff: 1, timeDiff: 25 },
    { pointDiff: 2, timeDiff: 15 },
    { pointDiff: 3, timeDiff: 7 },
    { pointDiff: 3, timeDiff: 8 },
    { pointDiff: 3, timeDiff: 8 },
    { pointDiff: 2, timeDiff: 8 },
    { pointDiff: 1, timeDiff: 73 }
  ];
  // 回弹段：过冲后回退修正
  const phaseRebound = [
    { pointDiff: -1, timeDiff: 200 },
    { pointDiff: -1, timeDiff: 9 },
    { pointDiff: -1, timeDiff: 24 },
    { pointDiff: -1, timeDiff: 24 },
    { pointDiff: -1, timeDiff: 41 }
  ];
  // 基准微调段：人手对准缺口的小步修正（点数动态调整区）
  const baseFineTune = [
    { pointDiff: 1, timeDiff: 15 },
    { pointDiff: 2, timeDiff: 17 },
    { pointDiff: 1, timeDiff: 89 },
    { pointDiff: 1, timeDiff: 15 },
    { pointDiff: 1, timeDiff: 17 },
    { pointDiff: 1, timeDiff: 17 },
    { pointDiff: 2, timeDiff: 7 },
    { pointDiff: 2, timeDiff: 25 },
    { pointDiff: 1, timeDiff: 17 },
    { pointDiff: 1, timeDiff: 6 },
    { pointDiff: 1, timeDiff: 8 },
    { pointDiff: 1, timeDiff: 8 },
    { pointDiff: 1, timeDiff: 24 },
    { pointDiff: 1, timeDiff: 8 },
    { pointDiff: 1, timeDiff: 17 },
    { pointDiff: 1, timeDiff: 7 },
    { pointDiff: 1, timeDiff: 8 },
    { pointDiff: 1, timeDiff: 17 },
    { pointDiff: 1, timeDiff: 424 }
  ];

  // ========== 2. 计算目标组数，动态生成微调段 ==========
  const fixedPointCount = phaseAccel.length + phaseDecel.length + phaseRebound.length + 1; // +1是起始点
  const minFineTune = Math.max(5, minPoints - fixedPointCount);
  const maxFineTune = Math.max(minFineTune, maxPoints - fixedPointCount);
  const targetFineTuneCount = Math.floor(minFineTune + Math.random() * (maxFineTune - minFineTune + 1));

  // 动态调整微调段点数
  let fineTune = [...baseFineTune];
  const diffCount = targetFineTuneCount - fineTune.length;

  if (diffCount > 0) {
    // 增加点数：随机插入1像素微调点
    for (let i = 0; i < diffCount; i++) {
      const idx = Math.floor(Math.random() * (fineTune.length + 1));
      const prevT = idx > 0 ? fineTune[idx - 1].timeDiff : 15;
      const nextT = idx < fineTune.length ? fineTune[idx].timeDiff : 15;
      fineTune.splice(idx, 0, {
        pointDiff: 1,
        timeDiff: Math.round((prevT + nextT) / 2)
      });
    }
  } else if (diffCount < 0) {
    // 减少点数：随机合并相邻点
    for (let i = 0; i < Math.abs(diffCount); i++) {
      if (fineTune.length <= 5) break;
      const idx = Math.floor(Math.random() * (fineTune.length - 1));
      fineTune.splice(idx, 2, {
        pointDiff: fineTune[idx].pointDiff + fineTune[idx + 1].pointDiff,
        timeDiff: fineTune[idx].timeDiff + fineTune[idx + 1].timeDiff
      });
    }
  }

  // 合并完整基础轨迹（不含起始点）
  const baseTrack = [...phaseAccel, ...phaseDecel, ...fineTune, ...phaseRebound];

  // ========== 3. 计算目标总时间（2~3秒，随位移正比分布） ==========
  // 位移映射：50px→2秒，300px→3秒，超出范围自动钳制
  const normX = Math.max(0, Math.min(1, (targetX - 50) / (300 - 50)));
  const baseTargetTime = minTime + normX * (maxTime - minTime);
  // 加入±8%随机波动，仍保持在2~3秒区间内
  const randomTimeOffset = baseTargetTime * (0.92 + Math.random() * 0.16);
  const targetTotalTime = Math.max(minTime, Math.min(maxTime, Math.round(randomTimeOffset)));

  // ========== 4. 位移与时间缩放 ==========
  const baseSumDx = baseTrack.reduce((s, p) => s + p.pointDiff, 0);
  const baseSumDt = baseTrack.reduce((s, p) => s + p.timeDiff, 0);
  const scaleX = targetX / baseSumDx;
  const scaleT = targetTotalTime / baseSumDt;

  // 执行缩放 + 单步时间随机扰动
  let track = baseTrack.map(item => {
    const dx = Math.round(item.pointDiff * scaleX);
    const rawDt = item.timeDiff * scaleT;
    const randomFactor = 1 - randomRange + Math.random() * 2 * randomRange;
    const dt = Math.max(1, Math.round(rawDt * randomFactor));
    return { pointDiff: dx, timeDiff: dt };
  });

  // 时间二次校准：保证总时间严格落在目标值（误差≤1ms）
  const currentSumDt = track.reduce((s, p) => s + p.timeDiff, 0);
  const timeError = targetTotalTime - currentSumDt;
  if (timeError !== 0) {
    // 误差分摊到微调段，不影响主运动节奏
    const fineStart = phaseAccel.length + phaseDecel.length;
    const fineEnd = fineStart + fineTune.length - 1;
    const step = timeError > 0 ? 1 : -1;
    let idx = fineStart;
    for (let i = 0; i < Math.abs(timeError); i++) {
      track[idx].timeDiff += step;
      idx++;
      if (idx > fineEnd) idx = fineStart;
    }
  }

  // ========== 5. 位移误差修正 ==========
  const currentSumDx = track.reduce((s, p) => s + p.pointDiff, 0);
  let posError = targetX - currentSumDx;
  const fineStartIdx = phaseAccel.length + phaseDecel.length;
  const fineEndIdx = fineStartIdx + fineTune.length - 1;
  let adjustIdx = fineStartIdx;

  while (posError !== 0) {
    if (posError > 0) {
      track[adjustIdx].pointDiff += 1;
      posError -= 1;
    } else {
      track[adjustIdx].pointDiff -= 1;
      posError += 1;
    }
    adjustIdx++;
    if (adjustIdx > fineEndIdx) adjustIdx = fineStartIdx;
  }

  // ========== 6. 添加起始点，输出结果 ==========
  track.unshift({ pointDiff: 0, timeDiff: 0 });
  const totalTime = track.reduce((s, p) => s + p.timeDiff, 0);

  return {
    'track': track,
    'totalTime': totalTime
  };
}
// 生成位移 150 像素的轨迹
const result = generateSlideTrack(150);
//console.log(result)
// console.log('数组组数：', result.track.length); // 44~85 之间随机
// console.log('总滑动时间：', result.totalTime, 'ms'); // 2000~3000 之间
// console.log('总位移校验：', result.track.reduce((s, p) => s + p.pointDiff, 0)); // 严格等于 150

function aes_encrypt(t, i, e) {

  const encrypted = CryptoJS["AES"]["encrypt"](t, i, {
    iv: e,
    mode: CryptoJS["mode"]["CBC"],
    padding: CryptoJS["pad"]["Pkcs7"]
  });

  // 完全你要的格式：encrypted["ciphertext"]["toString"]()["toUpperCase"]()
  const hexUpper = encrypted["ciphertext"]["toString"]()["toUpperCase"]();
  return hexUpper;
}
function aes_decrypt(cipherText, key, iv) {
  // 如果传入的是 hex 字符串，先转换为 CipherParams
  if (typeof cipherText === 'string') {
    cipherText = CryptoJS.lib.CipherParams.create({
      ciphertext: CryptoJS.enc.Hex.parse(cipherText)
    });
  }
  const decrypted = CryptoJS["AES"]["decrypt"](cipherText, key, {
    iv: iv,
    mode: CryptoJS["mode"]["CBC"],
    padding: CryptoJS["pad"]["Pkcs7"]
  });
  // 转UTF-8原始明文字符串返回
  return decrypted.toString(CryptoJS.enc.Utf8);
}
// pppp = 'b864bc3e58b5f00115f63525ab12846ad009bf9e1e2fa4d53b06843c0392104c3f5827589ad2b6bf7a3458acd9b94739911610726ddc2c635d5633b319e5aa68865db8969c068369bfbce2ccb1304a8b5df23def19b8f94b1c266e83ec53d9777645b2641acf697d4641a9a909392682dbb67b963328084dd3c78191d63a696a9f981d4dcf2d4b9b6b6755a7cea593663c5f09a0bb3f52be6b6d3985e5f2d5d6bc27f71a47a91a15d494b9552ce4d2dbc30ae344438b2b21ad0d0a15d0bcea78dc414e541461220125f0f102390b8024'
// iiii = { '$super': { '$super': {} }, 'words': [1735406945, 1684353901, 1815503981, 862348399], 'sigBytes': 16 }
// console.log(aes_decrypt(pppp,iiii, iiii))
data = {
  'token': "ffa877c0f389468c8d1c801076bb65d0",
  'captchaType': 1,
  'points': '{"token":"ffa877c0f389468c8d1c801076bb65d0","captchaType":1,"points":[{"x":143,"y":0}],"rates":[{"pointDiff":0,"timeDiff":0},{"pointDiff":0,"timeDiff":5},{"pointDiff":1,"timeDiff":14},{"pointDiff":3,"timeDiff":6},{"pointDiff":3,"timeDiff":8},{"pointDiff":4,"timeDiff":8},{"pointDiff":7,"timeDiff":8},{"pointDiff":7,"timeDiff":8},{"pointDiff":9,"timeDiff":8},{"pointDiff":10,"timeDiff":8},{"pointDiff":9,"timeDiff":8},{"pointDiff":13,"timeDiff":8},{"pointDiff":12,"timeDiff":8},{"pointDiff":10,"timeDiff":7},{"pointDiff":8,"timeDiff":9},{"pointDiff":7,"timeDiff":8},{"pointDiff":4,"timeDiff":8},{"pointDiff":3,"timeDiff":8},{"pointDiff":2,"timeDiff":7},{"pointDiff":1,"timeDiff":9},{"pointDiff":1,"timeDiff":40},{"pointDiff":2,"timeDiff":8},{"pointDiff":3,"timeDiff":7},{"pointDiff":3,"timeDiff":9},{"pointDiff":4,"timeDiff":8},{"pointDiff":4,"timeDiff":8},{"pointDiff":3,"timeDiff":7},{"pointDiff":3,"timeDiff":8},{"pointDiff":1,"timeDiff":8},{"pointDiff":1,"timeDiff":8},{"pointDiff":1,"timeDiff":17},{"pointDiff":1,"timeDiff":256},{"pointDiff":1,"timeDiff":7},{"pointDiff":2,"timeDiff":18},{"pointDiff":1,"timeDiff":15},{"pointDiff":1,"timeDiff":16},{"pointDiff":-1,"timeDiff":696},{"pointDiff":-1,"timeDiff":68},{"pointDiff":0,"timeDiff":4573}],"dragTime":5930,"time":1782185620960,"finger":3881141159}',
  'rates': "OGQ4NWxrNHdqanhvbzl4aA==",
  'dragTime': 5930,
  'time': Date.now(),
  'finger': 3881141159

}
function get_pb2_cp2(t) {
  t = JSON.stringify(t)
  console.log("t = ", t)

  buffer = new TextEncoder().encode(get_randomstr());
  base64 = getBase64Str(buffer.buffer);
  n = base64
  console.log("get_randomstr() = ", get_randomstr())
  console.log("n =", n)

  e = encrypt(n, PUBLIC_KEY)
  console.log("e = ", e)

  i = getBase64Parse(n)
  console.log("i =", i)

  c = i

  t = aes_encrypt(t, i, c)
  console.log("t = ")
  console.log(t)
  return {
    'pb': t,
    'cp': e,
    'i': c
  }
}
get_pb2_cp2(data)


function getBase64Parse(base64Str) {
  return CryptoJS['enc']['Base64']['parse'](base64Str)
}
function getBase64Str(o) {
  const bytes = new Uint8Array(o);
  let binary = '';
  const len = bytes.byteLength;
  for (let i = 0; i < len; i++) {
    binary += String.fromCharCode(bytes[i]);
  }
  return btoa(binary);
}

// 调用
