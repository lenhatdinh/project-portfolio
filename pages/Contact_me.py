import streamlit as st

st.set_page_config("Contact me", layout="centered")

st.columns([1.4, 2, 1])[1].title("Contact me")

def verify_and_send():
    email, message = st.session_state["email"], st.session_state["message"]

    if not email:
        response_holder.warning("Your email is missing.")

    elif not message:
        response_holder.warning("Your message is missing.")

    else:
        send_email(email, message)
        response_holder.info(
            "Sucessfully sent!"
            f"\n- Your email: {email}"
            f"\n- Your message: {message}"
        )
        st.session_state["email"] = ""
        st.session_state["message"] = ""

def send_email(email, message):
    pass

with st.form(key="contact-form"):
    st.text_input("Your email:", key="email")
    st.text_area("Your message:", key="message")

    response_holder = st.container()
    response_holder.form_submit_button(
        "Send",
        use_container_width=True,
        on_click=verify_and_send,
    )