from xhs_prompt_template import system_template_text, user_template_text
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.output_parsers import PydanticOutputParser
from 小红书model import Xiaohongshu
def generate_xiaohongshu (theme, video_length, creativity, additional_info):
    prompt = ChatPromptTemplate.from_messages(
        [
            ( "system",system_template_text),
            ("user", user_template_text),
        ]
    )
    model = ChatOpenAI(
                       openai_api_key=api_key,
                       temperature=creativity)
    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    chain = prompt | model | output_parser
    search = WikipediaAPIWrapper(lang="zh")
    search_result = search.run(theme)
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme,
        "duration": video_length,
        "wikipedia_search": search_result,
        "additional_info": additional_info
    })
    return result
# print(generate_xiaohongshu("bread", 3, "0.8"))
