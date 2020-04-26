/**
 *
 * This file was generated with Adobe XD React Exporter
 * Exporter for Adobe XD is written by: Johannes Pichler <j.pichler@webpixels.at>
 *
 **/

import React from "react";
import Svg, {
  Defs,
  Pattern,
  Image,
  ClipPath,
  Rect,
  G,
  Path,
  Circle,
  Text,
  TSpan
} from "react-native-svg";
/* Adobe XD React Exporter has dropped some elements not supported by react-native-svg: style, filter */

const ScheduleConfirmationComponent = () => (
  <Svg width={375} height={812} viewBox="0 0 375 812">
    <Defs>
      <Pattern
        id="e"
        preserveAspectRatio="xMidYMid slice"
        width="100%"
        height="100%"
        viewBox="0 0 750 750"
      >
        <Image width={750} height={750} xlinkHref="/Users/ina/Desktop/0.jpeg" />
      </Pattern>
      <ClipPath id="i">
        <Rect width={375} height={812} />
      </ClipPath>
    </Defs>
    <G id="h" className="a">
      <Rect className="b" width={375} height={812} />
      <G className="n" transform="matrix(1, 0, 0, 1, 0, 0)">
        <Rect
          className="c"
          width={302}
          height={275}
          rx={5}
          transform="translate(37 197)"
        />
      </G>
      <G transform="translate(0 -4)">
        <G transform="translate(0 -239)">
          <G className="m" transform="matrix(1, 0, 0, 1, 0, 243)">
            <Path
              className="d"
              d="M5,0H245a5,5,0,0,1,5,5V80a5,5,0,0,1-5,5H5a5,5,0,0,1-5-5V5A5,5,0,0,1,5,0Z"
              transform="translate(63 224)"
            />
          </G>
          <G transform="translate(77 480)">
            <Circle className="d" cx={30} cy={30} r={30} />
            <Circle
              className="e"
              cx={28}
              cy={28}
              r={28}
              transform="translate(2 2)"
            />
          </G>
          <G transform="translate(-6 162)">
            <Text className="f" transform="translate(156 344)">
              <TSpan x={0} y={0}>
                {"William Eustis"}
              </TSpan>
            </Text>
            <Text className="g" transform="translate(156 363)">
              <TSpan x={0} y={0}>
                {"Psychicatrist at Carle"}
              </TSpan>
            </Text>
          </G>
        </G>
        <Text className="h" transform="translate(188 344)">
          <TSpan x={-57.701} y={0}>
            {"March 3rd, 2020 "}
          </TSpan>
          <TSpan x={-29.344} y={18}>
            {"11:00 AM"}
          </TSpan>
        </Text>
        <G transform="translate(0 -6)">
          <G className="l" transform="matrix(1, 0, 0, 1, 0, 10)">
            <Rect
              className="i"
              width={215}
              height={43}
              rx={5}
              transform="translate(80 379)"
            />
          </G>
          <Text className="j" transform="translate(95 416)">
            <TSpan x={0} y={0}>
              {"Make an appointment"}
            </TSpan>
          </Text>
        </G>
        <Text className="k" transform="translate(164 446)">
          <TSpan x={0} y={0}>
            {"Cancel"}
          </TSpan>
        </Text>
      </G>
    </G>
  </Svg>
);

export default ScheduleConfirmationComponent;
