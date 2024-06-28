import streamlit as st
from utils import generate_xiaohongshu

# 使用 use_column_width 参数来使图像的宽度适应当前列的宽度
st.image("biaoti.png", use_column_width=True)

chinese_text = {
    "title": "爆款短视频AI创作助手——小红豆",
    "description": "<div style='background-color: #FFEFEF; padding: 20px; border-radius: 10px; font-size:15px; margin_bottom:20px;'>"
                   "💗 Hi，我是小红豆🔴，你的AI创作助手～<br>💗 我可以帮你创作爆款短视频标题和文案，适用于抖音、小红书🍠等短视频平台 <br>💰 祝你早日成为爆款达人！</div>",
    "theme_input_label": "请输入你想生成的视频主题🎵",
    "video_length_input_label": "请输入你想生成的视频时长🕙（单位：分钟）",
    "creativity_slider_label": "设置小红豆的创造力（数字越大，小红豆越有想象力；数字越小，小红豆越严谨）",
    "generate_button_label": "开始创作",
    "missing_theme_message": "输入视频主题，小红豆才能帮你创作哦",
    "invalid_video_length_message": "视频时长需要大于0.1分钟",
    "creating_message": "小红豆正在努力创作中...请稍等🚀",
    "success_message": "小红豆为你创作完成！✨",
    "title1_label": "爆款短视频标题1",
    "title2_label": "爆款短视频标题2",
    "title3_label": "爆款短视频标题3",
    "title4_label": "爆款短视频标题4",
    "title5_label": "爆款短视频标题5",
    "content_label": "爆款短视频正文",
    "contact_expander_label": "Happy Playing😎✌️",
    "contact_message": "作者：Jixin",
    "add":"（可选填) 视频内容关键词，输入之后可以让小红豆更好地了解你的想法，更精准输出内容",
    "api":"请输入OPENAI api密钥：",
    "get_api":"请输入你的openai api密钥"
}

english_text = {
    "title": "Popular Short Video AI Creative Assistant——Red Bean",
    "description": "<div style='background-color: #FFEFEF; padding: 20px; border-radius: 10px; font-size:15px; margin_bottom:20px;'>"
                   "💗  Hi, I'm Red Bean 🔴, your AI Creative Assistant!<br>💗 I can help you create social media video titles and scripts, perfect for platforms like TikTok🎵 and Xiaohongshu 🍠 <br>💰 Wishing you swift success in becoming a super influencer！</div>",
    "theme_input_label": "Please enter the theme of the video you want to generate 🎵",
    "video_length_input_label": "Please enter the video length you want to generate 🕙 (unit: minutes)",
    "creativity_slider_label": "Set Red Bean's creativity (the larger the number, the more imaginative Little Red Bean is; the smaller the number, the more rigorous Little Red Bean is)",
    "generate_button_label": "Start creating",
    "missing_theme_message": "Enter the video theme so Red Bean can help you create",
    "invalid_video_length_message": "Video length needs to be greater than 0.1 minutes",
    "creating_message": "Red Bean is working hard to create... Please wait 🚀",
    "success_message": "Red Bean has created for you! ✨",
    "title1_label": "Popular Social Media Video Title 1",
    "title2_label": "Popular Social Media Video Title 2",
    "title3_label": "Popular Social Media Video Title 3",
    "title4_label": "Popular Social Media Video Title 4",
    "title5_label": "Popular Social Media Video Title 5",
    "content_label": "Popular Social Media Video Content",
    "contact_expander_label": "Happy Playing😎✌️",
    "contact_message": "Author: Jixin",
    "api":"please input OPENAI api key：",
    "get_api":"please input your OPENAI aip key",
    "add":"(Optional) Video content keywords. After inputting, Red Bean can better understand your thoughts and output the content more accurately."
}

st.markdown("<style>.stTextInput>label {margin-top: 20px;}</style>", unsafe_allow_html=True)



# 切换语言按钮
if "language" not in st.session_state:
    st.session_state.language = "chinese"

if st.button("Switch Language"):
    if st.session_state.language == "chinese":
        st.session_state.language = "english"
    else:
        st.session_state.language = "chinese"


# 根据当前语言选择显示文本内容
if st.session_state.language == "english":
    text = english_text
else:
    text = chinese_text

with st.sidebar:
    openai_api_key=st.text_input(text["api"], type="password")
    st.markdown("[获取openai密钥](https://platform.openai.com/api-keys)")
    st.image("小红豆.png", use_column_width=True)
    st.markdown(text["contact_expander_label"])
    st.markdown(text["contact_message"])


# 在页面中显示文本内容
st.title(text["title"])
st.markdown(text["description"], unsafe_allow_html=True)

theme = st.text_input(text["theme_input_label"])

video_length = st.number_input(text["video_length_input_label"], min_value=0.1, max_value=5.0, step=0.1, value=3.0)

additional_info = st.text_input(text["add"])

creativity = st.slider(text["creativity_slider_label"], 0.0, 2.0, 1.0, 0.1)

submit = st.button(text["generate_button_label"])
if submit and not openai_api_key:
    st.info(text["get_api"])
    st.stop()
if submit and not theme:
    st.info(text["missing_theme_message"])
    st.stop()
if submit and not video_length >=0.1:
    st.info(text["invalid_video_length_message"])
    st.stop()
if submit:
    with st.spinner(text["creating_message"]):
        result = generate_xiaohongshu(theme, video_length, creativity, additional_info)
        st.divider()
        st.success(text["success_message"])
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(f"#### {text['title1_label']}")
        st.write(result.titles[0])
        st.markdown(f"#### {text['title2_label']}")
        st.write(result.titles[1])
        st.markdown(f"#### {text['title3_label']}")
        st.write(result.titles[2])
        st.markdown(f"#### {text['title4_label']}")
        st.write(result.titles[3])
        st.markdown(f"#### {text['title5_label']}")
        st.write(result.titles[4])
    with right_column:
        st.markdown(f"#### {text['content_label']}")
        st.write(result.content)



