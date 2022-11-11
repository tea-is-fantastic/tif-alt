def nav_theme():
    return """
import {DefaultTheme} from '@react-navigation/native';
import {
  cardColor,
  disabledColor,
  primaryColor,
  secondaryColor,
} from './colors';

const navigationTheme = {
  ...DefaultTheme,
  colors: {
    ...DefaultTheme.colors,
    primary: primaryColor,
    accent: secondaryColor,
    background: backgroundColor,
    surface: cardColor,
    disabled: disabledColor,
  },
};

export default navigationTheme;
"""
