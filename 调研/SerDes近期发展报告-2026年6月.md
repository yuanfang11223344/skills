# SerDes 近期发展报告（2025–2026）

> 生成日期：2026年6月15日
> 覆盖范围：学术论文、行业会议、公司动态、市场趋势
> 数据来源：IEEE Xplore、ISSCC/CICC/DesignCon、TrendForce、各公司官网

---

## 一、技术演进：从112G到224G的全面跨越

### 1.1 速率路线图

AI 工作负载对片间互连带宽的需求正以每两年翻倍的速度增长。SerDes 技术作为高速互连的物理层基石，正在经历从 **112G PAM4** 到 **224G PAM4** 的关键代际切换：

| 世代 | 速率 | 典型协议 | 工艺节点 | 量产状态 |
|------|------|----------|----------|----------|
| 第三世代 | 56G PAM4 | PCIe 4.0, 25G Ethernet | 7nm | **已量产**（2020-） |
| 第四世代 | 112G PAM4 | PCIe 5.0/6.0, 400G Ethernet | 5nm | **主流量产**（2023-） |
| 第五世代 | 224G PAM4 | PCIe 7.0, 800G/1.6T Ethernet, UALink | 3nm | **送样/小规模量产**（2025-2026） |
| 第六世代（前瞻） | 448G PAM4 | 3.2T Ethernet | 2nm+ | **预研中**（DesignCon 2026 首展示） |

### 1.2 核心技术突破

**（1）收发机架构演进**

IEEE 固态电路期刊（JSSC）2025年特刊《High-Performance Wireline Transceiver Circuits》系统总结了长距 SerDes 的最新架构趋势：

- **ADC-based 接收机成为224G标配**：在更高奈奎斯特频率下，传统纯模拟均衡器（CTLE+DFE）的补偿能力不足，ADC（通常为6-8bit，56GS/s以上）+全数字均衡（FFE+DFE）成为主流方案
- **5nm CMOS 上实现 212.5Gb/s PAM4**：文献报告在5nm FinFET工艺上实现了能效比2.2pJ/b、>46dB信道补偿能力的收发机，为224G量产铺平了道路
- **MIMO跨通道串扰消除（FEXT Cancellation）**：RFSoC平台上实现了2路DAC/ADC-based 2×2 MIMO PAM4收发机，通过MMSE-DFE消除远端串扰，为高密度互连提供新思路

**（2）反射消除与均衡技术**

2025年ScienceDirect论文提出了一种结合4-tap浮点FFE和2-tap投机预判决DFE的自适应均衡方案，专门针对**高速SerDes接收机中的反射干扰（Reflection Cancellation）**问题。这在224G速率下尤为重要——信号波长变短，PCB阻抗不连续造成的反射效应显著加剧。

**（3）PCB材料升级**

随着SerDes速率从112G跃迁至224G，PCB基材的介质损耗成为关键瓶颈。松下**Megtron 7**系列覆铜板成为行业首选方案，其低损耗特性使112G/224G SerDes系统的信号完整性得到显著改善。

---

## 二、全球竞争格局：六大阵营的SerDes战争

TrendForce在2026年3月发布的深度报告指出，AI互连的物理层正经历"拐点"，SerDes市场格局正在重塑：

### 2.1 竞争矩阵

| 阵营 | 代表厂商 | 核心竞争力 | 224G进展 | 市场定位 |
|------|----------|-----------|----------|----------|
| **垂直整合霸主** | **Broadcom** | 全球SerDes市占率>70%，全速率IP全覆盖 | Tomahawk 6 (3nm, 200G SerDes) 2025年发货 | 交换机ASIC+SerDes生态 |
| **光子学破局者** | **Marvell** | PCIe SerDes节奏领先Broadcom，2nm硅IP平台 | 2025年发布首款2nm IP，含224G光/电SerDes | 硅光子+scale-up互连 |
| **IP授权双雄** | **Synopsys** (第一) / **Cadence** (第二) | 112G-224G可授权IP，硅验证成熟 | Cadence：>40dB插损下CEI-224G-LR互操作，pre-FEC BER=5E-08 | 赋能fabless客户 |
| **新晋挑战者** | **联发科(MediaTek)** | 自主研发224G SerDes，进入Google TPU生态 | TPU v8e "Zebrafish" 已流片验证；400G IP计划2026推出 | AI ASIC+SerDes IP |
| **收购入场者** | **高通(Qualcomm)** | 收购Alphawave获224G SerDes技术 | 收购后整合阶段 | 数据中心SerDes市场新势力 |
| **中国自主突破** | **澜起科技(Montage)** | 32GT/s PCIe 5.0 Retimer量产，64GT/s送样 | 128GT/s (PCIe 7.0)研发中 | 中国SerDes/Retimer龙头 |

### 2.2 关键事件时间线

```
2025 Q1-Q2
├── Marvell 发布首款 2nm 硅IP平台（含全系列SerDes）
├── DesignCon 2025：Broadcom+Samtec 联合展示200Gbps SerDes+Si-Fly铜缆方案
│
2025 Q3-Q4
├── Broadcom Tomahawk 6 (3nm, 200G SerDes) 开始发货
├── 联发科 Google TPU v8e (224G SerDes) Tape-out
├── Cadence @ ECOC 2025：展示224G SerDes长距/短距互操作
│
2026 Q1
├── DesignCon 2026：首次展示448 Gbps PAM4概念验证
├── 澜起科技发布PCIe 6.0 AEC（自研SerDes+DSP架构）
│
2026 Q2
├── TrendForce发布"AI互连拐点"深度研报
├── 澜起科技宣布第三子代MRCD/MDB芯片工程研发计划
│
预期 2026 H2
├── AI芯片大规模过渡至224G SerDes
├── PCIe 7.0规范定型，128GT/s SerDes进入送样阶段
```

---

## 三、NVIDIA开放IP：生态地震的深层影响

NVIDIA在2025年宣布将**NVLink Fusion SerDes IP**开放给IC和IP设计合作伙伴，这是近年来SerDes行业最具颠覆性的动作：

### 3.1 为什么要开放？

- **Scale-up瓶颈**：NVIDIA的GPU-to-GPU互连（NVLink）需要专属物理层，但随着AI集群规模指数增长（万卡→十万卡→百万卡），封闭的NVLink生态在成本和供应链上有压力
- **UALink标准化**：行业联盟推动的UALink 1.0需要统一的物理层标准，NVIDIA开放IP是为了在标准制定中保持影响力
- **制程成本压力**：自研SerDes的维护成本随工艺演进急剧上升（3nm→2nm），开放IP可分摊研发投入

### 3.2 行业影响

| 受益者 | 影响 |
|--------|------|
| **Synopsys/Cadence** | 获得NVIDIA SerDes IP授权后，可整合进自有IP组合，赋能更多客户 |
| **定制ASIC厂商** | 可直接使用经过硅验证的NVLink SerDes IP，降低研发风险 |
| **Broadcom** | 失去SerDes独家壁垒，面临IP授权的价格竞争 |
| **Marvell** | 与NVLink生态竞争scale-up市场，加速光子学布局以差异化 |
| **联发科/高通** | 获得与NVLink互操作的IP基础，加速AI芯片布局 |

---

## 四、中国市场动态

### 4.1 澜起科技（Montage Technology）

澜起科技是中国SerDes/Retimer领域的绝对龙头，其最新动态：

| 时间 | 事件 | 意义 |
|------|------|------|
| 2025年1月 | 发布PCIe 6.0 Retimer芯片（64GT/s） | 中国首个PCIe 6.0 Retimer，送样测试中 |
| 2026年1月 | 发布自研SerDes+DSP架构的PCIe 6.0 AEC | 以Retimer为核心的有源电缆方案 |
| 2026年5月 | 确认"高速SerDes技术为核心技术之一" | 布局PCIe 7.0 (128GT/s) |
| 2026年规划 | 第三子代MRCD/MDB芯片工程研发 | 服务器内存接口芯片持续迭代 |

澜起科技已构建了从**32GT/s (PCIe 5.0) → 64GT/s (PCIe 6.0) → 128GT/s (PCIe 7.0)** 的完整SerDes技术路线，验证状态均为"已量产出货→送样测试→研发中"，节奏清晰。

### 4.2 PCIe 7.0 AEC 战略意义

澜起科技率先推出基于PCIe 6.x/CXL 3.x的AEC，核心优势在于：
- **自研SerDes + 创新DSP架构**：不依赖第三方IP，成本可控
- **OSFP-XD高密度封装**：支持64 GT/s x16传输
- **应用场景**：机箱内/跨板卡/跨节点/机柜间——覆盖AI超节点系统互连需求

> **行业预期**：PCIe 6.0 Retimer预计2027年进入正式规模应用，澜起科技有望在这一窗口期抢占全球市场份额。

---

## 五、技术前沿：224G之后的方向

### 5.1 448G PAM4 (1.6T/3.2T Ethernet)

DesignCon 2026首次展示了**448 Gbps PAM4 SerDes**概念验证。速率从224G到448G的翻倍面临三大挑战：
- **信道带宽**：更高奈奎斯特频率下铜缆衰减急剧增大，需要CPO或硅光子方案
- **ADC功耗**：采样率翻倍导致ADC功耗指数增长，需探索sub-ADC架构和时分交织技术
- **信号完整性**：在448G速率下，PCB布线长度被压缩到厘米级，chiplet和2.5D/3D封装成为必需

### 5.2 共封装光学（CPO）

Broadcom Tomahawk 6已集成CPO选项，Cadence提出**"一个224G SerDes统一scale-up和scale-out"**的理念。CPO的核心价值在于：
- 消除PCB走线的带宽瓶颈
- 降低SerDes驱动功耗（省去长距铜缆驱动）
- 光引擎与ASIC共封装，实现Tbps级互连密度

### 5.3 Chiplet + UCIe 2.0

Qualitas Semiconductor（韩国）在2025-2026年实现了多项突破：
- **4nm UCIe 2.0 + PCIe 6.0 PHY IP**：已授权给美国领先AI半导体公司
- **IP-SoC 2026**：推出面向AI/HPC的PCIe 6.0 & UCIe 2.0 PHY组合方案
- 标准化chiplet互连物理层正在加速落地，4nm节点已验证

### 5.4 铜退光进的物理极限

TrendForce指出：**传统铜互联在400G以上已触及物理极限**，技术必然走向光传输领域。这是所有SerDes玩家的共同判断——未来的投入焦点不是"要不要做光"，而是"何时做、以什么架构做"。

---

## 六、市场展望

### 6.1 市场规模

| 指标 | 数据 |
|------|------|
| 当前全球市场规模 | ~5亿美元（2025） |
| CAGR (2025-2033) | 9.8% |
| 2033年预计规模 | 11.8亿美元 |
| 增长驱动 | AI/ML数据中心、5G/6G基础设施、自动驾驶 |
| 最大应用领域 | 数据中心（Data Center） |
| 主导产品形态 | 嵌入式SerDes (Embedded SerDes) |
| 增长最快地区 | 亚太（中国、韩国、台湾） |
| 下一增长点 | 224G→448G架构、CPO光子引擎、Chiplet SerDes |

### 6.2 关键趋势预判

1. **224G SerDes 将在2026年下半年成为AI芯片主流配置**——NVIDIA下一代GPU、Google TPU v8e、AMD MI400等都将搭载224G I/O
2. **SerDes IP授权市场将加速增长**——NVIDIA开放IP、联发科/高通入局，IP竞争将拉低授权成本，使更多fabless公司能使用顶规SerDes
3. **PCIe 7.0 Retimer 将在2027年进入商用**——澜起科技、Astera Labs、Broadcom三强争霸
4. **CPO 从技术验证走向小规模商用**——首先在超大规模数据中心内部署，2028年后向通用市场渗透
5. **硅光子SerDes 是终极形态**——Marvell和Intel的硅光子方案代表了铜互连的终局替代

---

## 七、总结与建议

SerDes行业正处于**14年以来最剧烈的技术代际切换**——从112G到224G不仅是速率的翻倍，更是架构（ADC-based）、封装（CPO）、生态（IP开放）和材料（Megtron 7/硅光子）的全方位转型。

| 维度 | 当前状态 | 1-2年趋势 |
|------|---------|-----------|
| 主流速率 | 112G PAM4 (量产) | → 224G PAM4 (2026 H2主流化) |
| 架构主导 | 模拟+混合信号 | → ADC-based + 全数字均衡 |
| 互连方案 | PCB铜缆 | → CPO共封装光学 (数据中心) |
| 竞争格局 | Broadcom一家独大 | → 六阵营混战 + NVIDIA IP开放搅局 |
| 中国市场 | 澜起科技引领 | → PCIe 6.0 Retimer/AEC 2027量产出海 |
| 工艺节点 | 5nm/3nm | → 3nm量产 + 2nm送样 |

**重点关注方向**：224G SerDes量产进度（Broadcom Tomahawk 6 ramp-up）、NVIDIA开放IP的客户采用情况、联发科TPU v8e流片结果、PCIe 7.0标准发布时间、CPO在超大规模数据中心的实际部署数据。

---

## 参考来源

- [IEEE JSSC: High-Performance Wireline Transceiver Circuits (2025)](https://ieeexplore.ieee.org/abstract/document/10892322)
- [TrendForce: SerDes Wars Heat Up (2026.03)](https://www.trendforce.com/news/2026/03/13/news-serdes-wars-heat-up-broadcom-marvell-mediatek-battle-for-ai-interconnect-supremacy/)
- [Cadence: How 224G SerDes Unifies Today's AI Fabrics](https://community.cadence.com/cadence_blogs_8/b/data-center/posts/how-224g-serdes-unifies-today-s-ai-fabrics)
- [澜起科技: PCIe 6.0 AEC解决方案 (2026.01)](https://www.c114.net.cn/chip/55039.html)
- [DesignCon 2025: Broadcom+Samtec 200Gbps Demo](https://kineticlive.samtec.com/support/videos/200-gbps-co-packaged-copper-channel-samtec-si-fly-hd-broadcom-serdes-1055985886/)
- [澜起科技: 高速SerDes技术是核心技术之一 (2026.05)](https://finance.eastmoney.com/a/202605263749912769.html)
- [TrendForce: The AI Interconnect Inflection Point](https://www.trendforce.com/research/download/RP260126WQ)
- [Qualitas Semiconductor: PCIe Gen6 & UCIe 2.0 PHY IP](https://www.q-semi.com/main)
- [SemiiPHub: Powering Scale Up and Scale Out with 224G SerDes](https://semiiphub.com/pulse/expert-perspectives/224g-serdes-ualink-ultra-ethernet)
- [ScienceDirect: 4-tap floating FFE + 2-tap DFE for wireline receiver (2025)](https://www.sciencedirect.com/science/article/abs/pii/S1879239125004503)

> 本报告使用了 `调研/` 目录中的 skill 工作流方法（发现→分析→产出），通过多源搜索、交叉验证、趋势分析和结构化输出生成。数据截止至2026年6月15日。
