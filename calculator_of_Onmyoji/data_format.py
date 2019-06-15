# coding: utf-8

import string


COL_INDEX = string.ascii_uppercase

MITAMA_COL_NAME_ZH = ['御魂序号', '御魂类型', '位置', '攻击',
                      '攻击加成', '防御', '防御加成', '暴击',
                      '暴击伤害', '生命', '生命加成', '效果命中',
                      '效果抵抗', '速度']

RESULT_HEADER = ['组合序号'] + MITAMA_COL_NAME_ZH

RESULT_HEADER_LEN = len(RESULT_HEADER)

RESULT_INDEX = {RESULT_HEADER[i]: COL_INDEX[i]
                for i in range(RESULT_HEADER_LEN)}

RESULT_COMB_HEADER = ['组合个数', '组合序号',
                      '暴击', '总攻击', '攻击x暴伤', '速度']

EXTEND_HEADER = ['式神基础攻击', '式神基础生命', '式神基础暴伤',
                 '总攻击', '总生命',
                 '攻击x暴伤', '生命×暴伤', '攻击x暴伤(+buff)']

EXTEND_INDEX = {EXTEND_HEADER[i]: COL_INDEX[i+RESULT_HEADER_LEN]
                for i in range(len(EXTEND_HEADER))}

MITAMA_PROPS = ['攻击', '攻击加成', '防御', '防御加成', '暴击',
                '暴击伤害', '生命', '生命加成', '效果命中',
                '效果抵抗', '速度']

MITAMA_ENHANCE = {"珍珠": {"加成类型": "防御加成", "加成数值": 30},
                  "骰子鬼": {"加成类型": "效果抵抗", "加成数值": 15},
                  "蚌精": {"加成类型": "效果命中", "加成数值": 15},
                  "魅妖": {"加成类型": "防御加成", "加成数值": 30},
                  "针女": {"加成类型": "暴击", "加成数值": 15},
                  "返魂香": {"加成类型": "效果抵抗", "加成数值": 15},
                  "雪幽魂": {"加成类型": "防御加成", "加成数值": 30},
                  "地藏像": {"加成类型": "生命加成", "加成数值": 15},
                  "蝠翼": {"加成类型": "攻击加成", "加成数值": 15},
                  "涅槃之火": {"加成类型": "生命加成", "加成数值": 15},
                  "三味": {"加成类型": "暴击", "加成数值": 15},
                  "魍魉之匣": {"加成类型": "效果抵抗", "加成数值": 15},
                  "被服": {"加成类型": "生命加成", "加成数值": 15},
                  "招财猫": {"加成类型": "防御加成", "加成数值": 30},
                  "反枕": {"加成类型": "防御加成", "加成数值": 30},
                  "轮入道": {"加成类型": "攻击加成", "加成数值": 15},
                  "日女巳时": {"加成类型": "防御加成", "加成数值": 30},
                  "镜姬": {"加成类型": "生命加成", "加成数值": 15},
                  "钟灵": {"加成类型": "生命加成", "加成数值": 15},
                  "狰": {"加成类型": "攻击加成", "加成数值": 15},
                  "火灵": {"加成类型": "效果命中", "加成数值": 15},
                  "鸣屋": {"加成类型": "攻击加成", "加成数值": 15},
                  "薙魂": {"加成类型": "生命加成", "加成数值": 15},
                  "心眼": {"加成类型": "攻击加成", "加成数值": 15},
                  "木魅": {"加成类型": "防御加成", "加成数值": 30},
                  "树妖": {"加成类型": "生命加成", "加成数值": 15},
                  "网切": {"加成类型": "暴击", "加成数值": 15},
                  "阴摩罗": {"加成类型": "攻击加成", "加成数值": 15},
                  "伤魂鸟": {"加成类型": "暴击", "加成数值": 15},
                  "破势": {"加成类型": "暴击", "加成数值": 15},
                  "镇墓兽": {"加成类型": "暴击", "加成数值": 15},
                  "狂骨": {"加成类型": "攻击加成", "加成数值": 15},
                  "幽谷响": {"加成类型": "效果抵抗", "加成数值": 15},
                  "兵主部": {"加成类型": "攻击加成", "加成数值": 15},
                  "青女房": {"加成类型": "暴击", "加成数值": 15},
                  "涂佛": {"加成类型": "生命加成", "加成数值": 15},
                  "飞缘魔": {"加成类型": "效果命中", "加成数值": 15},
                  "土蜘蛛": {"加成类型": "", "加成数值": 0},
                  "胧车": {"加成类型": "", "加成数值": 0},
                  "荒骷髅": {"加成类型": "", "加成数值": 0},
                  "地震鲶": {"加成类型": "", "加成数值": 0},
                  "蜃气楼": {"加成类型": "", "加成数值": 0},
                  }

MITAMA_TYPES = list(MITAMA_ENHANCE.keys())

MITAMA_GROWTH = {"攻击加成": {"最小成长值": 2.4,
                                  "副属性最大值": 26,
                                  "主属性": 55},
                 "生命加成": {"最小成长值": 2.4,
                                  "副属性最大值": 26,
                                  "主属性": 55},
                 "防御加成": {"最小成长值": 2.4,
                                  "副属性最大值": 26,
                                  "主属性": 55},
                 "效果命中": {"最小成长值": 3.2,
                                  "副属性最大值": 32,
                                  "主属性": 55},
                 "效果抵抗": {"最小成长值": 3.2,
                                  "副属性最大值": 32,
                                  "主属性": 55},
                 "暴击": {"最小成长值": 2.4,
                            "副属性最大值": 26,
                            "主属性": 55},
                 "暴击伤害": {"最小成长值": 3.2,
                                  "副属性最大值": 24,
                                  "主属性": 89},
                 "速度": {"最小成长值": 2.4,
                            "副属性最大值": 18,
                            "主属性": 57},
                 "攻击": {"最小成长值": 21.6,
                            "副属性最大值": 162,
                            "主属性": 486},
                 "防御": {"最小成长值": 4,
                            "副属性最大值": 30,
                            "主属性": 104},
                 "生命": {"最小成长值": 91.2,
                            "副属性最大值": 684,
                            "主属性": 2052},
                 }

MITAMA_ESP_EXTEND_HEADER = ["输出类有效条数", "奶盾类有效条数",
                            "命中类有效条数", "双堆类有效条数",
                            "混合类有效条数"]

MITAMA_ESP = {"输出类有效条数": ['攻击加成', '暴击', '速度', '暴击伤害'],
              "奶盾类有效条数": ['生命加成', '暴击', '速度', '暴击伤害'],
              "命中类有效条数": ['速度', '效果命中'],
              "双堆类有效条数": ['速度', '效果命中', '效果抵抗'],
              "混合类有效条数": ['速度', '效果命中', '效果抵抗',
                                        '攻击加成', '生命加成',
                                        '暴击', '暴击伤害'],
              }

ATTACK_MITAMA_TYPE = [t for t, e in list(MITAMA_ENHANCE.items())
                      if e['加成类型'] in ['', '攻击加成', '暴击']]

SUIT_ID_TO_NAME = {300002: '雪幽魂', 300003: '地藏像', 300004: '蝠翼',
                   300006: '涅槃之火', 300007: '三味', 300008: '魍魉之匣',
                   300009: '被服', 300010: '招财猫', 300011: '反枕',
                   300012: '轮入道', 300013: '日女巳时', 300014: '镜姬',
                   300015: '钟灵', 300018: '狰', 300019: '火灵', 300020: '鸣屋',
                   300021: '薙魂', 300022: '心眼', 300023: '木魅', 300024: '树妖',
                   300026: '网切', 300027: '阴摩罗', 300029: '伤魂鸟',
                   300030: '破势', 300031: '镇墓兽', 300032: '珍珠',
                   300033: '骰子鬼', 300034: '蚌精', 300035: '魅妖',
                   300036: '针女', 300039: '返魂香', 300048: '狂骨',
                   300049: '幽谷响', 300050: '土蜘蛛', 300051: '胧车',
                   300052: '荒骷髅', 300053: '地震鲶', 300054: '蜃气楼'}
