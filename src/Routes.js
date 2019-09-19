import React from 'react';
import { Route, Switch } from 'react-router-dom';
import Gifs from './Gifs';
import Detail from './Detail';
import HowToFace from "./HowToFace";


export default function Routes(props) {
    return (
        <Switch>
            <Route path="/how-to-cut-out-a-face" component={ HowToFace } />
            <Route path="/:type" component={ Detail } />
            <Route path="/" component={ Gifs } />
        </Switch>
    );
}
