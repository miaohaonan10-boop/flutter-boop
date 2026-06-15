"""
济宁 家乡旅行推荐 / 지닝 고향 여행 추천 앱
"""

import tkinter as tk
from tkinter import ttk

THEME_COLORS = {
    "bg": "#F5F0EB",
    "card": "#FFFFFF",
    "text": "#3E2723",
    "subtext": "#8D6E63",
    "muted": "#BCAAA4",
    "tag_bg": "#EFEBE9",
    "tag_text": "#5D4037",
    "shadow": "#D0C8C0",
    "hc": "#8B4513",
    "ac": "#D2A679",
}


CITY = {
    "name_zh": "济宁", "name_ko": "지닝",
    "tagline_zh": "孔孟之乡 · 运河之都", "tagline_ko": "공자·맹자의 고향 · 운하의 수도",
    "icon": "🏠", "header_color": "#8B4513", "accent_color": "#D2A679",
    "desc_zh": '济宁市位于山东省西南部，是儒家文化发源地，素有「孔孟之乡、运河之都」的美誉。总面积1.1万平方公里，常住人口约830万。',
    "desc_ko": '지닝시는 산둥성 서남부에 위치한 유교 문화의 발상지입니다. 총면적 1.1만 km², 상주인구 약 830만 명.',
    "highlights": [{"zh": "儒家文化发源地", "ko": "유교 문화 발상지"}, {"zh": "京杭大运河重要节点", "ko": "경항 대운하 중요 거점"}, {"zh": "中国优秀旅游城市", "ko": "중국 우수 관광 도시"}, {"zh": "国家级历史文化名城", "ko": "국가급 역사문화 명성"}],
    "attractions": [
            {"name_zh": "曲阜三孔 (孔庙·孔府·孔林)", "name_ko": "취푸 삼공", "desc_zh": "世界文化遗产，祭祀孔子的祠庙建筑群。", "desc_ko": "세계문화유산으로 공자를 제사하는 사당 건축군입니다.", "tags": ["世界遗产", "5A景区", "儒家文化"], "famous": "大成殿·重光门·孔子墓", "img_icon": "🏛️", "img_color": "#8B0000"},
            {"name_zh": "邹城孟庙孟府", "name_ko": "쩌우청 맹묘·맹부", "desc_zh": "祭祀亚圣孟子的庙宇和府邸。始建于北宋。", "desc_ko": "아성 맹자를 제사하는 사당과 저택입니다.", "tags": ["全国文保", "4A景区", "儒家文化"], "famous": "棂星门·亚圣殿·孟府大堂", "img_icon": "⛩️", "img_color": "#4A2511"},
            {"name_zh": "微山湖旅游区", "name_ko": "웨이산호 관광구", "desc_zh": "中国北方最大的淡水湖，夏季万亩荷花盛开。", "desc_ko": "중국 북방 최대 담수호입니다.", "tags": ["5A景区", "自然风光", "湿地生态"], "famous": "万亩荷塘·微山岛", "img_icon": "🪷", "img_color": "#2E7D32"},
            {"name_zh": "水泊梁山风景区", "name_ko": "수박 양산 풍경구", "desc_zh": "《水浒传》故事发源地。", "desc_ko": "『수호전』 이야기의 발원지.", "tags": ["4A景区", "历史文化", "水浒文化"], "famous": "忠义堂·黑风口", "img_icon": "🏔️", "img_color": "#5D4037"},
            {"name_zh": "太白楼", "name_ko": "태백루", "desc_zh": "纪念唐代大诗人李白的建筑。", "desc_ko": "당나라 대시인 이백을 기념하는 건축물.", "tags": ["历史文化", "名人故居", "3A景区"], "famous": "太白楼诗碑·李白纪念馆", "img_icon": "🏯", "img_color": "#B8860B"}
        ],
    "foods": [
            {"name_zh": "甏肉干饭", "name_ko": "벙러우 간판", "desc_zh": "济宁最具代表性的传统小吃，五花肉慢火炖煮。", "desc_ko": "지닝 대표 전통小吃.", "features": "百年老店 · 非遗美食", "img_icon": "🍖", "img_color": "#BF360C"},
            {"name_zh": "孔府菜", "name_ko": "공부 요리", "desc_zh": "中国最高规格官府菜之一。", "desc_ko": "중국 최고 규격 관부 요리.", "features": "官府菜 · 非物质文化遗产", "img_icon": "🍲", "img_color": "#33691E"},
            {"name_zh": "济宁夹饼", "name_ko": "지닝 자삥", "desc_zh": "街头最受欢迎的早餐，自由搭配。", "desc_ko": "길거리 최고 인기 아침식사.", "features": "街头小吃 · 百搭自由", "img_icon": "🥙", "img_color": "#F57F17"},
            {"name_zh": "糁汤", "name_ko": "싼탕", "desc_zh": "传统早餐汤品，鲜香暖胃。", "desc_ko": "전통 아침 수프.", "features": "百年传承 · 营养早餐", "img_icon": "🍵", "img_color": "#6D4C41"},
            {"name_zh": "玉堂酱菜", "name_ko": "위탕 장채", "desc_zh": "中华老字号，始创1714年。", "desc_ko": "중화노자호, 1714년 창립.", "features": "中华老字号 · 省级非遗", "img_icon": "🫙", "img_color": "#558B2F"}
        ],
    "routes": [
            {"name_zh": "一日文化精华游", "name_ko": "1일 문화 정수 투어", "duration": "1天", "stops": ["上午：曲阜三孔", "中午：孔府菜", "下午：邹城孟庙孟府", "傍晚：太白楼"]},
            {"name_zh": "两日深度体验游", "name_ko": "2일 심층 체험 투어", "duration": "2天", "stops": ["Day1：三孔 → 孔府菜 → 尼山圣境", "Day2：微山湖乘船 → 甏肉干饭 → 返程"]},
            {"name_zh": "三日全景游", "name_ko": "3일 전경 투어", "duration": "3天", "stops": ["Day1：三孔 → 尼山圣境", "Day2：孟庙 → 微山湖", "Day3：水泊梁山 → 太白楼 → 返程"]}
        ],
}

class TravelApp:
    def __init__(self, root):
        self.root = root
        self.root.title(f"{CITY['name_zh']} 家乡旅行推荐 / {CITY['name_ko']} 고향 여행 추천")
        self.root.geometry("1100x750")
        self.root.minsize(900, 600)
        self.root.configure(bg=THEME_COLORS["bg"])
        self.current_page = None
        self.main = tk.Frame(self.root, bg=THEME_COLORS["bg"])
        self.main.pack(fill=tk.BOTH, expand=True)
        self._build_layout()

    def _clear_main(self):
        self.root.unbind_all("<MouseWheel>")
        for w in self.main.winfo_children():
            w.destroy()

    def _build_layout(self):
        c = CITY
        hc = THEME_COLORS["hc"]
        ac = THEME_COLORS["ac"]

        sidebar = tk.Frame(self.main, bg="#2C1A14", width=210)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        sidebar.pack_propagate(False)

        st = tk.Frame(sidebar, bg="#2C1A14")
        st.pack(fill=tk.X, pady=(30, 12), padx=18)
        tk.Label(st, text=c['icon'], font=("Segoe UI Emoji", 38), bg="#2C1A14").pack()
        tk.Label(st, text=c['name_zh'], font=("Microsoft YaHei", 22, "bold"), fg="#FFF8E1", bg="#2C1A14").pack(pady=(2, 0))
        tk.Label(st, text=c['name_ko'], font=("Malgun Gothic", 12), fg=ac, bg="#2C1A14").pack()

        tk.Frame(sidebar, bg=ac, height=1).pack(fill=tk.X, padx=18, pady=8)

        nav_items = [
            ("home", "\U0001f3e0  首页 / \ud648"),
            ("attractions", "\U0001f3ef  景点 / \uad00\uad11\uc9c0"),
            ("foods", "\U0001f35c  美食 / \ubbf8\uc2dd"),
            ("routes", "\U0001f5fa\ufe0f  路线 / \uacbd\ub85c"),
            ("ai_info", "\U0001f916  AI 使用"),
        ]
        self._nav_btns = {}
        for key, label in nav_items:
            btn = tk.Button(sidebar, text=label, font=("Microsoft YaHei", 12, "bold"),
                          bg="#2C1A14", fg="#A1887F",
                          activebackground="#45302B", activeforeground="#FFFFFF",
                          bd=0, cursor="hand2", anchor="w", padx=22, pady=12,
                          command=lambda k=key: self._page(k))
            btn.pack(fill=tk.X)
            self._nav_btns[key] = btn

        tk.Label(sidebar, text="\u00a9 2025 \u5bb6\u4e61\u65c5\u884c\nFlutter \uacfc\uc81c", font=("Microsoft YaHei", 8),
                fg="#5D4037", bg="#2C1A14", justify=tk.CENTER).pack(side=tk.BOTTOM, pady=20)

        self._content = tk.Frame(self.main, bg=THEME_COLORS["bg"])
        self._content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self._page("home")

    def _page(self, page_key):
        self.current_page = page_key
        hc = THEME_COLORS["hc"]
        ac = THEME_COLORS["ac"]
        for key, btn in self._nav_btns.items():
            active = key == page_key
            btn.configure(bg="#45302B" if active else "#2C1A14",
                         fg=ac if active else "#A1887F")
        for w in self._content.winfo_children():
            w.destroy()
        if page_key == "home": self._render_home()
        elif page_key == "attractions": self._render_attractions()
        elif page_key == "foods": self._render_foods()
        elif page_key == "routes": self._render_routes()
        elif page_key == "ai_info": self._render_ai_info()

    def _title(self, text, sub=""):
        f = tk.Frame(self._content, bg=THEME_COLORS["bg"])
        f.pack(fill=tk.X, padx=35, pady=(30, 8))
        tk.Label(f, text=text, font=("Microsoft YaHei", 22, "bold"), fg="#3E2723", bg=THEME_COLORS["bg"]).pack(anchor="w")
        if sub:
            tk.Label(f, text=sub, font=("Malgun Gothic", 10), fg=THEME_COLORS["subtext"], bg=THEME_COLORS["bg"]).pack(anchor="w")
        tk.Frame(self._content, bg="#D7CCC8", height=2).pack(fill=tk.X, padx=35, pady=(4, 18))

    def _scrollable(self):
        cv = tk.Canvas(self._content, bg=THEME_COLORS["bg"], bd=0, highlightthickness=0)
        sb = ttk.Scrollbar(self._content, orient="vertical", command=cv.yview)
        sf = tk.Frame(cv, bg=THEME_COLORS["bg"])
        sf.bind("<Configure>", lambda e: cv.configure(scrollregion=cv.bbox("all")))
        cv.create_window((0, 0), window=sf, anchor="nw", width=860)
        cv.configure(yscrollcommand=sb.set)
        cv.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")
        cv.bind("<Enter>", lambda e: cv.bind_all("<MouseWheel>",
                lambda ev: cv.yview_scroll(int(-1 * (ev.delta / 120)), "units")))
        cv.bind("<Leave>", lambda e: cv.unbind_all("<MouseWheel>"))
        return sf

    def _card(self, parent):
        shadow = tk.Frame(parent, bg="#D0C8C0")
        card = tk.Frame(shadow, bg=THEME_COLORS["card"], bd=0)
        card.pack(padx=2, pady=2)
        return shadow

    def _render_home(self):
        c = CITY
        hc = THEME_COLORS["hc"]
        ac = THEME_COLORS["ac"]
        self._title(f"{c['name_zh']}欢迎您 / {c['name_ko']}에 오신 것을 환영합니다")
        sf = self._scrollable()

        card = self._card(sf)
        card.pack(fill=tk.X, padx=30, pady=(0, 14))
        tk.Label(card.children['!frame'], text=f"🏙️  {c['name_zh']}概况 / {c['name_ko']} 개요",
                font=("Microsoft YaHei", 15, "bold"), fg=hc, bg=THEME_COLORS["card"]).pack(anchor="w", padx=22, pady=(18, 8))
        tk.Label(card.children['!frame'], text=c['desc_zh'], font=("Microsoft YaHei", 11), fg="#4E342E",
                bg=THEME_COLORS["card"], wraplength=780, justify=tk.LEFT).pack(anchor="w", padx=22)
        tk.Label(card.children['!frame'], text=c['desc_ko'], font=("Malgun Gothic", 10), fg=THEME_COLORS["subtext"],
                bg=THEME_COLORS["card"], wraplength=780, justify=tk.LEFT).pack(anchor="w", padx=22, pady=(4, 18))

        hl = self._card(sf)
        hl.pack(fill=tk.X, padx=30, pady=(0, 14))
        tk.Label(hl.children['!frame'], text="✨ 城市亮点 / 도시 하이라이트", font=("Microsoft YaHei", 15, "bold"),
                fg=hc, bg=THEME_COLORS["card"]).pack(anchor="w", padx=22, pady=(18, 12))
        hi = tk.Frame(hl.children['!frame'], bg=THEME_COLORS["card"])
        hi.pack(fill=tk.X, padx=22, pady=(0, 18))
        for i, h in enumerate(c['highlights']):
            t = tk.Frame(hi, bg=ac)
            t.pack(side=tk.LEFT, padx=(0 if i == 0 else 10, 0), pady=4)
            tk.Label(t, text=f"  {h['zh']}  ", font=("Microsoft YaHei", 11, "bold"), fg="#FFFFFF", bg=ac).pack(padx=10, pady=6)
            tk.Label(t, text=h['ko'], font=("Malgun Gothic", 9), fg="#3E2723", bg=ac).pack(padx=10, pady=(0, 6))

    def _render_attractions(self):
        c = CITY
        hc = THEME_COLORS["hc"]
        ac = THEME_COLORS["ac"]
        self._title("代表旅游景点 / 대표 관광지")
        sf = self._scrollable()
        for a in c['attractions']:
            card = self._card(sf)
            card.pack(fill=tk.X, padx=30, pady=(0, 16))

            img_area = tk.Frame(card.children['!frame'], bg=a.get('img_color', hc), height=100)
            img_area.pack(fill=tk.X)
            img_area.pack_propagate(False)
            tk.Label(img_area, text=a.get('img_icon', '🏯'), font=("Segoe UI Emoji", 48),
                    bg=a.get('img_color', hc)).place(relx=0.5, rely=0.5, anchor="center")

            hd = tk.Frame(card.children['!frame'], bg=a.get('img_color', hc))
            hd.pack(fill=tk.X)
            tk.Label(hd, text=f"  {a['name_zh']}", font=("Microsoft YaHei", 14, "bold"),
                    fg="#FFFFFF", bg=a.get('img_color', hc)).pack(side=tk.LEFT, padx=18, pady=(10, 5))
            tk.Label(hd, text=f"{a['name_ko']}  ", font=("Malgun Gothic", 10),
                    fg="#FFE0B2", bg=a.get('img_color', hc)).pack(side=tk.RIGHT, padx=18, pady=(10, 5))

            bd = tk.Frame(card.children['!frame'], bg=THEME_COLORS["card"])
            bd.pack(fill=tk.X, padx=18, pady=12)
            tk.Label(bd, text=a['desc_zh'], font=("Microsoft YaHei", 11), fg="#4E342E",
                    bg=THEME_COLORS["card"], wraplength=780, justify=tk.LEFT).pack(anchor="w")
            tk.Label(bd, text=a['desc_ko'], font=("Malgun Gothic", 10), fg=THEME_COLORS["subtext"],
                    bg=THEME_COLORS["card"], wraplength=780, justify=tk.LEFT).pack(anchor="w", pady=(3, 0))

            bt_row = tk.Frame(bd, bg=THEME_COLORS["card"])
            bt_row.pack(fill=tk.X, pady=(10, 0))
            for tag in a['tags']:
                tag_f = tk.Frame(bt_row, bg=THEME_COLORS["tag_bg"])
                tag_f.pack(side=tk.LEFT, padx=(0, 6))
                tk.Label(tag_f, text=f" #{tag} ", font=("Microsoft YaHei", 9),
                        fg=THEME_COLORS["tag_text"], bg=THEME_COLORS["tag_bg"]).pack(padx=6, pady=2)
            tk.Label(bt_row, text=f"   📍 必看：{a['famous']}", font=("Microsoft YaHei", 9),
                    fg=ac, bg=THEME_COLORS["card"]).pack(side=tk.LEFT, padx=(8, 0))

    def _render_foods(self):
        c = CITY
        hc = THEME_COLORS["hc"]
        self._title("代表美食 / 대표 음식")
        sf = self._scrollable()
        for f in c['foods']:
            card = self._card(sf)
            card.pack(fill=tk.X, padx=30, pady=(0, 16))

            left_bar = tk.Frame(card.children['!frame'], bg=f.get('img_color', hc), width=100)
            left_bar.pack(side=tk.LEFT, fill=tk.Y)
            left_bar.pack_propagate(False)
            tk.Label(left_bar, text=f.get('img_icon', '🍜'), font=("Segoe UI Emoji", 40),
                    bg=f.get('img_color', hc)).pack(expand=True)

            right = tk.Frame(card.children['!frame'], bg=THEME_COLORS["card"])
            right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=18, pady=14)

            nr = tk.Frame(right, bg=THEME_COLORS["card"])
            nr.pack(fill=tk.X)
            tk.Label(nr, text=f"🍜 {f['name_zh']}", font=("Microsoft YaHei", 15, "bold"),
                    fg=hc, bg=THEME_COLORS["card"]).pack(side=tk.LEFT)
            tk.Label(nr, text=f" ({f['name_ko']})", font=("Malgun Gothic", 10),
                    fg=THEME_COLORS["muted"], bg=THEME_COLORS["card"]).pack(side=tk.LEFT, padx=(5, 0))

            tk.Label(right, text=f['desc_zh'], font=("Microsoft YaHei", 11), fg="#4E342E",
                    bg=THEME_COLORS["card"], wraplength=680, justify=tk.LEFT).pack(anchor="w", pady=(8, 2))
            tk.Label(right, text=f['desc_ko'], font=("Malgun Gothic", 10), fg=THEME_COLORS["subtext"],
                    bg=THEME_COLORS["card"], wraplength=680, justify=tk.LEFT).pack(anchor="w")

            feat_f = tk.Frame(right, bg=f.get('img_color', "#FF6F00"))
            feat_f.pack(anchor="w", pady=(10, 0))
            tk.Label(feat_f, text=f"  🏷 {f['features']}  ", font=("Microsoft YaHei", 9, "bold"),
                    fg="#FFFFFF", bg=f.get('img_color', "#FF6F00")).pack(padx=8, pady=3)

    def _render_routes(self):
        c = CITY
        icons = ["☀️", "🌅", "🌟"]
        route_colors = ["#E65100", "#1565C0", "#6A1B9A"]
        self._title("推荐旅行路线 / 추천 여행 코스")
        sf = self._scrollable()
        for i, r in enumerate(c['routes']):
            card = self._card(sf)
            card.pack(fill=tk.X, padx=30, pady=(0, 16))
            rc = route_colors[i]

            hd = tk.Frame(card.children['!frame'], bg=rc)
            hd.pack(fill=tk.X)
            tk.Label(hd, text=f"  {icons[i]}  {r['name_zh']}  ({r['name_ko']})",
                    font=("Microsoft YaHei", 14, "bold"), fg="#FFFFFF", bg=rc).pack(side=tk.LEFT, padx=18, pady=(12, 5))
            tk.Label(hd, text=f"{r['duration']}  ", font=("Malgun Gothic", 10),
                    fg="#FFE0B2" if i == 0 else "#BBDEFB" if i == 1 else "#E1BEE7", bg=rc).pack(side=tk.RIGHT, padx=18, pady=(12, 5))

            bd = tk.Frame(card.children['!frame'], bg=THEME_COLORS["card"])
            bd.pack(fill=tk.X, padx=22, pady=18)
            for j, s in enumerate(r['stops']):
                step = tk.Frame(bd, bg=THEME_COLORS["card"])
                step.pack(fill=tk.X, pady=4)
                nf = tk.Frame(step, bg=rc, width=30, height=30)
                nf.pack(side=tk.LEFT, padx=(0, 12))
                nf.pack_propagate(False)
                tk.Label(nf, text=str(j + 1), font=("Microsoft YaHei", 11, "bold"),
                        fg="#FFFFFF", bg=rc).pack(expand=True)
                tk.Label(step, text=s, font=("Microsoft YaHei", 11), fg="#4E342E",
                        bg=THEME_COLORS["card"], anchor="w").pack(side=tk.LEFT)

    def _render_ai_info(self):
        self._title("AI 使用内容 / AI 활용 내용")
        card = self._card(self._content)
        card.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)

        tk.Label(card.children['!frame'], text="🤖 AI 辅助开发说明", font=("Microsoft YaHei", 15, "bold"),
                fg="#3E2723", bg=THEME_COLORS["card"]).pack(anchor="w", padx=22, pady=(18, 12))

        items = [
            ("📝 内容生成 / 콘텐츠 생성", "景区介绍文本由AI辅助生成和润色。\\n관광지 소개 텍스트는 AI가 생성 및 윤색했습니다."),
            ("🌐 双语翻译 / 이중 언어 번역", "中韩双语翻译由AI辅助完成。\\n중한 이중 언어 번역은 AI가 보조했습니다."),
            ("🗺️ 路线规划 / 경로 계획", "旅行路线由AI根据景点距离等因素优化。\\n여행 경로는 AI가 최적화했습니다."),
            ("💻 代码框架 / 코드 프레임", "程序代码框架由AI辅助搭建。\\n프로그램 코드 프레임은 AI의 보조로 구축되었습니다."),
            ("🎨 界面设计 / UI 디자인", "配色方案和布局设计由AI辅助生成。\\n색상 구성 및 레이아웃은 AI가 보조했습니다."),
        ]
        for title, desc in items:
            it = tk.Frame(card.children['!frame'], bg="#FAF6F2")
            it.pack(fill=tk.X, padx=22, pady=(0, 10))
            tk.Label(it, text=title, font=("Microsoft YaHei", 12, "bold"),
                    fg="#5D4037", bg="#FAF6F2").pack(anchor="w", padx=16, pady=(12, 4))
            tk.Label(it, text=desc, font=("Microsoft YaHei", 11), fg="#4E342E",
                    bg="#FAF6F2", wraplength=760, justify=tk.LEFT).pack(anchor="w", padx=16, pady=(0, 12))

        bt = tk.Frame(card.children['!frame'], bg="#FFF8E1")
        bt.pack(fill=tk.X, padx=22, pady=(12, 18))
        tk.Label(bt, text="※ AI 사용 고지 / AI 使用声明", font=("Microsoft YaHei", 9, "bold"),
                fg="#F57F17", bg="#FFF8E1").pack(anchor="w", padx=16, pady=(12, 4))
        tk.Label(bt, text="본 프로그램의 텍스트 콘텐츠, 번역, 코드 및 디자인 요소는 AI 기술을 활용하여 생성되었습니다.\\n本程序的文本内容、翻译、代码及设计元素均借助AI技术生成。",
                font=("Microsoft YaHei", 9), fg="#E65100", bg="#FFF8E1",
                wraplength=760, justify=tk.LEFT).pack(anchor="w", padx=16, pady=(0, 12))


def main():
    root = tk.Tk()
    app = TravelApp(root)
    root.update_idletasks()
    sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
    w, h = root.winfo_width(), root.winfo_height()
    root.geometry(f"+{(sw - w) // 2}+{(sh - h) // 2}")
    root.mainloop()


if __name__ == "__main__":
    main()
