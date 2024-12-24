from util.crawling import get_data
import streamlit as st
import requests
import os
import asyncio

st.set_page_config(page_title="알고리즘 프로젝트", page_icon="💬")

class Basic:

    def __init__(self):

        self.server_url = "http://localhost:8000"

        if "name" not in st.session_state:
            st.session_state["name"] = None

        if "session_disable" not in st.session_state:
            st.session_state["session_disable"] = True

        if "session_id_input_disable" not in st.session_state:
            st.session_state["session_id_input_disable"] = False

    def session_enable(self):

        if st.session_state["name"]:
            st.session_state["session_disable"] = False
            st.session_state["session_id_input_disable"] = True
        return

    def session_disable(self):
        st.session_state["session_disable"] = True
        st.session_state["session_id_input_disable"] = False
        return

    def send_query_to_server(self, session_id, user_query):
        """서버에 요청을 보내고 응답을 받습니다."""

        name = st.session_state["name"]

        data = {"session_id": session_id, "messages": user_query}

        response = requests.post(f"{self.server_url}/{name}/", json=data)
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Error communicating with the server.")
            return None
        
    async def main(self):

        st.sidebar.divider()

        name =selected_items = st.sidebar.multiselect("이름 선택", ["hyeonsang"] , disabled=st.session_state["session_id_input_disable"])

        if name:

            st.session_state["name"] = name[0]

        session_start = st.sidebar.button(
            "세션 시작",
            disabled=st.session_state["session_id_input_disable"],
            on_click=self.session_enable,
        )

        if session_start:

            st.sidebar.info(f"{name[0]}님 세션을 시작합니다.")



        problem_numbers = st.chat_input(
            placeholder="문제 번호를 입력하세요.",
            disabled=st.session_state["session_disable"],
        )
        if problem_numbers:

            stat , content , inputs , ouputs = get_data(problem_numbers)

            if stat:
                st.write(content)
                st.write(inputs)
                st.write(ouputs)

            else:
                st.write("요청 에러 문제 숫자만 입력해주세요.")
            


if __name__ == "__main__":
    obj = Basic()
    # obj.main()
    asyncio.run(obj.main())
