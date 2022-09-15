import streamlit as st

def mode1(name, number, sourcerName):

    name = name.replace(" ", "%20")
    sourcerName = sourcerName.replace(" ", "%20")

    message = "https://api.whatsapp.com/send?phone=" + number + "&text=Hello%20" + name + "%2C%20%0A%0ANice%20to%20be%20in%20contact%2C%20I'm%20from%20Progress%20Property%2C%20we%20find%20HMO%20properties%20for%20company%20let%20on%20behalf%20of%20our%20clients%20helping%20them%20grow%20their%20portfolios.%20%0A%0AWe%20have%20been%20in%20contact%20with%20you%20before%20and%20we're%20interested%20in%20seeing%20what%20new%20business%20we%20can%20do!%0A%0ALook%20forward%20to%20hearing%20back%20from%20you.%20Thanks.%20%0A%0A" + sourcerName +"%0A%0AProgress%20Property%20Services%20Ltd%20%0Ahttps%3A%2F%2Fprogresspropertyservices.co"

    return message

def mode2(name, number, location, sourcerName):

    name = name.replace(" ", "%20")
    location = location.replace(" ", "%20")
    sourcerName = sourcerName.replace(" ", "%20")

    message = "https://api.whatsapp.com/send?phone=" + number + "&text=Hey%20" + name + "%2C%20%0A%0AMy%20company%20Progress%20Property%20Services%20has%20previously%20been%20in%20contact%20with%20you%20in%20regards%20to%20your%20search%20for%20properties%20located%20around%20" + location + ".%20%0A%0AWe%20have%20several%20new%20deals%20available%20and%20are%20hoping%20there%20is%20new%20business%20that%20can%20be%20done%20with%20you%20if%20you%20are%20still%20interested%20%3F%20%0A%0AKind%20regards%20%0A%0A" + sourcerName + "%0A%0AProgress%20Property%20Services%20Ltd%20%0Ahttps%3A%2F%2Fprogresspropertyservices.co"

    return message

def mode3(name, number, sourcerName):

    name = name.replace(" ", "%20")
    sourcerName = sourcerName.replace(" ", "%20")

    message = "https://api.whatsapp.com/send?phone=" + number +  "&text=Hello%2C%20nice%20to%20be%20in%20contact%20" + name +"%0A%0AI’m%20representing%20Progress%20Property%20Services%20Ltd%20-%20specialists%20in%20finding%20high%20yielding%20company%20let%20opportunities.%20%0A%0AWe%20came%20across%20your%20company%20and%20we%20are%20interested%20in%20what%20business%20we%20can%20do!%20%20%0A%0ALook%20forward%20to%20hearing%20from%20you%2C%20Thanks%0A%0A"+sourcerName+"%20%7C%20Business%20Development%20Consultant%20%0A%0AProgress%20Property%20Services%20Ltd%20%0Ahttps%3A%2F%2Flinktr.ee%2Fprogressproperty"

    return message

def mode4(name, number, sourcerName):

    name = name.replace(" ", "%20")
    sourcerName = sourcerName.replace(" ", "%20")

    message = "https://api.whatsapp.com/send?phone=" +number+"&text=%20Hi%20"+name+"%2C%20%0A%20%0AWe%20are%20mainly%20assisting%20management%20companies%20in%20London.%20A%20lot%20of%20our%20clients%20are%20companies%20who%20are%20looking%20to%20house%20working%20professionals%2C%20Social%20housing%20providers%2C%20lettings%20agents%20…%20etc.%0A%20%0AWe%20started%20doing%20business%203%20years%20ago%20and%20have%20seen%20good%20results%20and%20are%20looking%20to%20invest%20more%20money%20into%20our%20property%20finding%20efforts%20in%20order%20to%20ensure%20that%20there%20are%20very%20few%20‘fit-for-purpose’%20properties%20in%20the%20UK%20that%20go%20overlooked.%20%0A%0A%0ACan%20you%20give%20me%20a%20similar%20scope%20for%20what%20you%20do%3F%20Do%20you%20deal%20with%20other%20companies%20similar%20to%20ourselves%20or%20are%20you%20a%20lettings%20company%20yourself%3F%0A%20%0AWill%20this%20be%20our%20best%20contact%20for%20us%20to%20send%20you%20our%20latest%20deals%3F%0A%20%0AThanks%0A%20%0A"+sourcerName+"%0A%20%0AProgress%20Property%20Services%20Ltd%20%0Ahttps%3A%2F%2Fprogresspropertyservices.co"

    return message


    

def main():
    st.title("Progress Property Investor Reachout")

    menu = ["Home","Mode 1", "Mode 2", "Mode 3","Mode 4"]

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

    elif choice == "Mode 3":
        st.subheader("Mode 3")
        st.caption("Mode 3: If you only have the name and number of the investor")

        mode3Name = st.text_input("Enter the name of the investor", placeholder="Investor Name")
        mode3Number = st.text_input("Enter the number of the investor", placeholder="Investor Number")
        mode3SourcerName = st.text_input("Enter the name of the Sourcer", placeholder="Sourcer Name")

        if st.button("Mode 3 Submit"):
            mode3Link = mode3(mode3Name, mode3Number, mode3SourcerName)

            st.info("[WhatsApp Link to Message Investor]("+mode3Link+")")


    elif choice == "Mode 4":
        st.subheader("Mode 4")
        st.caption("Mode 4: If you only have the name and number of the investor")

        mode4Name = st.text_input("Enter the name of the investor", placeholder="Investor Name")
        mode4Number = st.text_input("Enter the number of the investor", placeholder="Investor Number")
        mode4SourcerName = st.text_input("Enter the name of the Sourcer", placeholder="Sourcer Name")

        if st.button("Mode 4 Submit"):
            mode4Link = mode4(mode4Name, mode4Number, mode4SourcerName)

            st.info("[WhatsApp Link to Message Investor]("+mode4Link+")")

if __name__ == "__main__":
    main()