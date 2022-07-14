import streamlit as st

def mode1(name, number, sourcerName):
    message = "https://api.whatsapp.com/send?phone=" + number + "&text=Hello%20" + name + "%2C%20%0A%0ANice%20to%20be%20in%20contact%2C%20I'm%20from%20Progress%20Property%2C%20we%20find%20HMO%20properties%20for%20company%20let%20on%20behalf%20of%20our%20clients%20helping%20them%20grow%20their%20portfolios.%20%0A%0AWe%20have%20been%20in%20contact%20with%20you%20before%20and%20we're%20interested%20in%20seeing%20what%20new%20business%20we%20can%20do!%0A%0ALook%20forward%20to%20hearing%20back%20from%20you.%20Thanks.%20%0A%0A" + sourcerName +"%0A%0AProgress%20Property%20Services%20Ltd%20%0Ahttps%3A%2F%2Fprogresspropertyservices.co"

    return message

def mode2(name, number, location, sourcerName):
    message = "https://api.whatsapp.com/send?phone=" + number + "&text=Hey%20" + name + "%2C%20%0A%0AMy%20company%20Progress%20Property%20Services%20has%20previously%20been%20in%20contact%20with%20you%20in%20regards%20to%20your%20search%20for%20properties%20located%20around%20" + location + ".%20%0A%0AWe%20have%20several%20new%20deals%20available%20and%20are%20hoping%20there%20is%20new%20business%20that%20can%20be%20done%20with%20you%20if%20you%20are%20still%20interested%20%3F%20%0A%0AKind%20regards%20%0A%0A" + sourcerName + "%0A%0AProgress%20Property%20Services%20Ltd%20%0Ahttps%3A%2F%2Fprogresspropertyservices.co"

    return message

def main():
    st.title("Progress Property Investor Reachout")

    menu = ["Home","Mode 1", "Mode 2"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.write("Mode 1: If you only have the name and number of the investor")
        st.write(" ")
        st.write("Mode 2: If you only have the name and number of the investor")

    elif choice == "Mode 1":
        st.subheader("Mode 1")
        st.caption("Mode 1: If you only have the name and number of the investor")

        mode1Name = st.text_input("Enter the name of the investor", placeholder="Investor Name")
        mode1Number = st.text_input("Enter the number of the investor", placeholder="Investor Number")
        mode1SourcerName = st.text_input("Enter the name of the Sourcer", placeholder="Sourcer Name")

        if st.button("Mode 1 Submit"):
            mode1Link = mode1(mode1Name, mode1Number, mode1SourcerName)

            st.info("[WhatsApp Link to Message Investor]("+mode1Link+")")

    elif choice == "Mode 2":
        st.subheader("Mode 2")
        st.caption("Mode 2: If you  have the name, number and location of the investor")

        mode2Name = st.text_input("Enter the name of the investor", placeholder="Investor Name")
        mode2Number = st.text_input("Enter the number of the investor", placeholder="Investor Number")
        mode2Location = st.text_input("Enter the location of interest of the investor", placeholder="Investor Location of Interest")

        mode2SourcerName = st.text_input("Enter the name of the Sourcer", placeholder="Sourcer Name")

        if st.button("Mode 2 Submit"):
            mode2Link = mode2(mode2Name, mode2Number, mode2Location, mode2SourcerName)

            st.info("[WhatsApp Link to Message Investor]("+mode2Link+")")

if __name__ == "__main__":
    main()