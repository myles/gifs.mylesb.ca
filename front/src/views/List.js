import React from 'react';
import { Link } from 'react-router-dom';
import LazyLoad from 'react-lazyload';
import { css } from 'glamor';

let GifListStyle = css({
  display: 'flex',
  flexWrap: 'wrap',
  justifyContent: 'center',
  alignItems: 'center',
  alignContent: 'space-around'
});

let GifDetailStyle = css({
  margin: '5px'
});

let GifDetailImageStyle = css({
  width: '500px'
});

let GifDetail = props =>
  <Link to={props.gif.slug} className={GifDetailStyle}>
    <img src={props.gif.image_url} alt="GIF"
         className={GifDetailImageStyle} />
  </Link>

class List extends React.Component {
  async getGifList() {
    let res = await fetch('/api.json');
    let json = await res.json();

    this.setState({ gif_list: json });
  };

  constructor(props) {
    super(props);

    this.getGifList();

    this.state = {
      gif_list: []
    };
  };

  render() {
    const gif_list = this.state.gif_list || [];

    return (
      <div className={GifListStyle}>
        {gif_list.map((gif, i) =>
          <LazyLoad height={200}>
            <GifDetail key={'gif-' + i} gif={gif} />
          </LazyLoad>
        )}
      </div>
    );
  };
};

export default List;
