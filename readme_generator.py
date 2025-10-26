import streamlit as st

st.set_page_config(layout="wide")
st.markdown(
    "<h1 style='text-align: center;'>README GENERATOR</h1>", unsafe_allow_html=True
)
st.caption(
    "<p style='text-align: center;'>Fill in the details below and generate a clean README.md with a single click.</p>",
    unsafe_allow_html=True,
)
# ================ CONSTANTS ================
class Constants:
    LICENCE_OPTIONS = [
        "MIT Licence",
        "GNU General Public Licence (GPL v3)",
        "GNU Lesser General Public Licence (LGPL v3)",
        "Mozilla Public Licence 2.0",
        "Creative Common (CC0/CC BY/variants)",
        "Unlicensed",
    ]


if "readme_content" not in st.session_state:
    st.session_state.readme_content = ""
if "missing_fields" not in st.session_state:
    st.session_state.missing_fields = []
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# ================ LAYOUT (SIDE BY SIDE) ================
col1, col2 = st.columns([1, 1], gap="large")

# ================ FORM SECTION ================
with col1:
    with st.form("readme_form", clear_on_submit=False):
        st.markdown(
            "<h4 style='text-align: center'>Project Details</h4>",
            unsafe_allow_html=True,
        )
        title = st.text_input("Project title", placeholder="e.g. warship-api-demo")

        description = st.text_area(
            "Description",
            placeholder="What does your project do? Why does it exist?",
            height=150,
        )

        installation_instructions = st.text_area(
            "Installation Instructions",
            placeholder="How should a user install and set up the project?",
            height=100,
        )

        features = st.text_area(
            "Features", placeholder="- Fast\n- Robust\n- Easy to use", height=130
        )

        lisense = st.selectbox("Select a License", Constants.LICENCE_OPTIONS, index=0)
        tech_stack = st.text_area(
            "Tech Stack", placeholder="- React\n- Express.js\n- Node.js ", height=130
        )

        submitted = st.form_submit_button("Generate README")

        data_dict = {
            "title": "",
            "description": "",
            "installation_instructions": "",
            "features": "",
            "lisense": "",
            "tech_stack": "",
        }
        # HANDLE FORM SUBMISSION
        if submitted:
            st.session_state.submitted = True
            data_dict.update(
                {
                    "title": title.strip(),
                    "description": description.strip(),
                    "installation_instructions": installation_instructions.strip(),
                    "features": features.strip(),
                    "lisense": lisense.strip(),
                    "tech_stack": tech_stack.strip(),
                }
            )
            # Error if any field is left empty
            is_missing = False
            missing_fields = []
            for name, value in data_dict.items():
                if not value:
                    is_missing = True
                    missing_fields.append(name)

            st.session_state.missing_fields = missing_fields

            if is_missing:
                st.error(
                    f'Please fill out the following fields: {", ".join(missing_fields).title().replace("_", " ")}'
                )
                st.session_state.readme_content = ""
            else:
                readme_content = f"""# {data_dict['title'].upper()}

## Description
{data_dict['description']}

## Installation Instructions
{data_dict['installation_instructions']}

## Features
{data_dict['features']}

## License
{data_dict['lisense']}

## Tech Stack
{data_dict['tech_stack']}
"""
                st.session_state.readme_content = readme_content

with col2:
    # ================ PREVIEW SECTION ================
    st.markdown(
        "<h4 style='text-align: center'>README.md Preview</h4>", unsafe_allow_html=True
    )
    if (
        st.session_state.submitted
        and not st.session_state.missing_fields
        and st.session_state.readme_content
    ):
        st.code(st.session_state.readme_content, language="markdown")
        st.download_button(
            "Download README.MD",
            data=st.session_state.readme_content,
            file_name="README.md",
            mime="text/markdown",
        )
        st.success("Press the button above to download your README.md.")

    elif st.session_state.submitted and st.session_state.missing_fields:
        st.info("Please complete all fields above and click **Generate README**.")
    else:
        st.info(
            "Complete the form and click **Generate README** to see a preview here."
        )
