import React from 'react';

class List extends React.Component {
  state = {
    gif_detail: {}
  }

  async getGifDetail() {
    let res = await fetch(`/${this.props.params.slug}/api.json`);
    let json = await res.json();

    this.setState({ gif_detail: json });
  }

  constructor(props) {
    super(props);

    this.getGifDetail();
  }

  render() {
    return (
      <div className="Detail">
        <img src={this.state.gif_detail.image_url} alt="GIF" />
      </div>
    );
  }
}

export default List;
