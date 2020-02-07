import React from "react";
import { graphql } from "gatsby";

// Components
import Layout from "../components/layout";
import Navigation from "../components/nav";
import SEO from "../components/seo";

class IndexPage extends React.Component {
  render() {
    const { data } = this.props;
    const siteTitle = data.site.siteMetadata.title;

    return (
      <Layout location={this.props.location} title={siteTitle}>
        <Navigation />
        <SEO
          title="Home"
          keywords={[`blog`, `gatsby`, `javascript`, `react`]}
        />
        <h1>Hello.</h1>
        <p>Welcome to my website, I hope you enjoy your stay!</p>
        <img
          style={{ margin: 0, border: "0.1px solid black" }}
          src="./torres.svg"
          alt="Hiking in Torres del Paine."
        />
        <small>
          The result of trying to convert a picture of me hiking in Torres del
          Paine National Park to an SVG image.
        </small>
      </Layout>
    );
  }
}

export const pageQuery = graphql`
  query {
    site {
      siteMetadata {
        title
      }
    }
  }
`;

export default IndexPage;
