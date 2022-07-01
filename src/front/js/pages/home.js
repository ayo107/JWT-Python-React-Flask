import React, { useContext } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";

export const Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="text-center mt-5">
			<h1>Inicia sesión, sino tienes cuenta...Creala...</h1>
			<p>
				<img src="http://3.bp.blogspot.com/-8vuHUqIo15E/VTDbP_MkrzI/AAAAAAAABc0/AA1kjvzMaYo/s1600/Bienvenida.png" />
			</p>
			
		</div>
	);
};
